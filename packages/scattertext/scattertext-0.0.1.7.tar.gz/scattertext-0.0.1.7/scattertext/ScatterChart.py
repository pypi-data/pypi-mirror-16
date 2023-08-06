import matplotlib.pyplot as plt
import numpy as np
from mpld3 import plugins, fig_to_html
from scipy.stats import rankdata

from scattertext.Scalers import percentile_min


def filter_bigrams_by_pmis(word_freq_df, threshold_coef=2):
	if len(word_freq_df.index) == 0:
		return word_freq_df

	is_bigram = np.array([' ' in word for word in word_freq_df.index])

	unigram_freq = word_freq_df[~is_bigram].sum(axis=1)
	bigram_freq = word_freq_df[is_bigram].sum(axis=1)
	bigram_prob = bigram_freq / bigram_freq.sum()
	unigram_prob = unigram_freq / unigram_freq.sum()

	def get_pmi(bigram):
		return np.log(
			bigram_prob[bigram] / np.product([unigram_prob[word] for word in bigram.split(' ')])
		) / np.log(2)

	low_pmi_bigrams = bigram_prob[bigram_prob.index.map(get_pmi) < threshold_coef * 2]
	return word_freq_df.drop(low_pmi_bigrams.index)


class NoWordMeetsTermFrequencyRequirementsError(Exception):
	pass


class ScatterChart:
	def __init__(self,
	             term_doc_matrix,
	             minimum_term_frequency=3,
	             jitter=0,
	             seed=0):
		'''
		:param term_doc_matrix: TermDocMatrix
		:param jitter: float
		:param seed: float
		'''
		self.term_doc_matrix = term_doc_matrix
		self.jitter = jitter
		self.minimum_term_frequency = minimum_term_frequency
		self.seed = seed
		np.random.seed(seed)

	def to_dict(self,
	            category,
	            scores=None,
	            transform=percentile_min):
		all_categories, other_categories = self._get_category_names(category)
		df = self._build_dataframe_for_drawing(all_categories, category, scores)
		df['x'], df['y'] = self._get_coordinates_from_transform_and_jitter_frequencies \
			(category, df, other_categories, transform)
		df['not cat freq'] = df[[x for x in other_categories]].sum(axis=1)
		json_df = df[['x', 'y', 'term']]
		json_df['cat25k'] = ((df[category + ' freq'] * 1. / df[category + ' freq'].sum()) * 25000)
		json_df['ncat25k'] = ((df['not cat freq'] * 1. / df['not cat freq'].sum()) * 25000)
		json_df['cat25k']=json_df['cat25k'].apply(np.round).astype(np.int)
		json_df['ncat25k']=json_df['ncat25k'].apply(np.round).astype(np.int)
		json_df['s'] = percentile_min(df['color_scores'])
		j = json_df.sort_values(by=['x', 'y', 'term']).to_dict(orient='records')
		return j

	def draw(self,
	         category,
	         num_top_words_to_annotate=4,
	         words_to_annotate=[],
	         scores=None,
	         transform=percentile_min):

		all_categories, other_categories = self._get_category_names(category)
		df = self._build_dataframe_for_drawing(all_categories, category, scores)
		x_data, y_data = self._get_coordinates_from_transform_and_jitter_frequencies \
			(category, df, other_categories, transform)
		df_to_annotate = df[(df['not category score rank'] <= num_top_words_to_annotate)
		                    | (df['category score rank'] <= num_top_words_to_annotate)
		                    | df['term'].isin(words_to_annotate)]
		words = list(df['term'])

		font = {'family': 'sans-serif',
		        'color': 'black',
		        'weight': 'normal',
		        'size': 'large'
		        }
		fig, ax = plt.subplots()
		plt.figure(figsize=(10, 10))
		plt.gcf().subplots_adjust(bottom=0.2)
		plt.gcf().subplots_adjust(right=0.2)

		points = ax.scatter(x_data,
		                    y_data,
		                    c=-df['color_scores'],
		                    cmap='seismic',
		                    s=10,
		                    edgecolors='none',
		                    alpha=0.9)
		tooltip = plugins.PointHTMLTooltip(points,
		                                   ['<span id=a>%s</span>' % w for w in words],
		                                   css='#a {background-color: white;}')
		plugins.connect(fig, tooltip)
		ax.set_ylim([-.2, 1.2])
		ax.set_xlim([-.2, 1.2])
		ax.xaxis.set_ticks([0., 0.5, 1.])
		ax.yaxis.set_ticks([0., 0.5, 1.])
		ax.set_ylabel(category.title() + ' Frequency Percentile', fontdict=font, labelpad=20)
		ax.set_xlabel('Not ' + category.title() + ' Frequency Percentile', fontdict=font, labelpad=20)

		for i, row in df_to_annotate.iterrows():
			# alignment_criteria = row['category score rank'] < row['not category score rank']
			alignment_criteria = i % 2 == 0
			horizontalalignment = 'right' if alignment_criteria else 'left'
			verticalalignment = 'bottom' if alignment_criteria else 'top'
			term = row['term']
			ax.annotate(term,
			            (x_data[i], y_data[i]),
			            size=15,
			            horizontalalignment=horizontalalignment,
			            verticalalignment=verticalalignment,
			            )
		# texts.append(
		# ax.text(row['dem freq scaled'], row['rep freq scaled'], row['word'])
		# )
		# adjust_text(texts, arrowprops=dict(arrowstyle="->", color='r', lw=0.5))
		plt.show()
		return df, fig_to_html(fig)

	def _get_coordinates_from_transform_and_jitter_frequencies(self, category, df, other_categories, transform):
		x_data_raw = transform(df[other_categories].sum(axis=1))
		y_data_raw = transform(df[category + ' freq'])
		x_data = self._add_jitter(x_data_raw)
		y_data = self._add_jitter(y_data_raw)
		return x_data, y_data

	def _add_jitter(self, vec):
		'''
		:param vec: array to jitter
		:return:
		'''
		if self.jitter == 0:
			return vec
		else:
			to_ret = vec + np.random.rand(1, len(vec))[0] * self.jitter
			return to_ret

	def _build_dataframe_for_drawing(self, all_categories, category, scores):
		df = self.term_doc_matrix.get_term_freq_df()
		df['category score'] = np.array(self.term_doc_matrix.get_rudder_scores(category))
		df['not category score'] = np.sqrt(2) - np.array(self.term_doc_matrix.get_rudder_scores(category))
		df['color_scores'] = scores \
			if scores is not None \
			else np.array(self.term_doc_matrix.get_scaled_f_scores(category))
		df = filter_bigrams_by_pmis(
			df[df[all_categories].sum(axis=1) > self.minimum_term_frequency],
			threshold_coef=3)
		if len(df) == 0: raise NoWordMeetsTermFrequencyRequirementsError()
		df['category score rank'] = rankdata(df['category score'], method='ordinal')
		df['not category score rank'] = rankdata(df['not category score'], method='ordinal')
		df = df.reset_index()
		return df

	def _get_category_names(self, category):
		other_categories = [val + ' freq' for _, val \
		                    in self.term_doc_matrix._category_idx_store.items() \
		                    if val != category]
		all_categories = other_categories + [category + ' freq']
		return all_categories, other_categories

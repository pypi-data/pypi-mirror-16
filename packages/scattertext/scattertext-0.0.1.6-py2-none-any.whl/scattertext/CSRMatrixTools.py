import numpy as np
from scipy.sparse import csr_matrix


class CSRMatrixFactory:
	def __init__(self):
		self.rows = []
		self.cols = []
		self.data = []
		self._max_col = 0
		self._max_row = 0

	def __setitem__(self, row_col, datum):
		'''
		:param row_col: (int, int)
		:param datum: int
		:return: None

		>>> mat_fact = CSRMatrixFactory()
		>>> mat_fact[3,1] = 1
		'''
		row, col = row_col
		self.rows.append(row)
		self.cols.append(col)
		self.data.append(datum)
		if row > self._max_row: self._max_row = row
		if col > self._max_col: self._max_col = col

	def get_csr_matrix(self):
		return csr_matrix((self.data, (self.rows, self.cols)),
		                  shape=(self._max_row + 1, self._max_col + 1),
		                  dtype=np.int32)


def delete_columns(mat, columns_to_delete):
	'''
	:param mat: csr_matrix
	:param columns_to_delete: list[int]
	:return: csr_matrix that is stripped of columns indices columns_to_delete

	>>> a = csr_matrix(np.array([[0, 1, 3, 0, 1, 0],
		                           [0, 0, 1, 0, 1, 1]])
	>>> delete_columns(a, [1,2]).todense()
	matrix([[0, 0, 1, 0],
          [0, 0, 1, 1]])
	'''
	column_mask = np.ones(mat.shape[1], dtype=bool)
	column_mask[columns_to_delete] = 0
	return mat.tocsc()[:, column_mask].tocsr()

import numpy as np

class NumPUtils:
    """
    A utility class for performing various calculations on a NumPy matrix.

    Attributes:
        matrix (ndarray): The NumPy matrix.

    Methods:
        mean: Calculates the mean of the matrix.
        median: Calculates the median of the matrix.
        corrcoef: Calculates the correlation coefficient of the matrix.
        var: Calculates the variance of the matrix.
        std: Calculates the standard deviation of the matrix.
        count_greater_than_mean: Counts the number of values in the matrix that are greater than the mean.
        std_of_values_greater_than_mean: Calculates the standard deviation of the values in the matrix that are greater than the mean.
    """

    def __init__(self, n, m):
        self.matrix = np.random.randint(100, size=(n, m))

    def mean(self):
        return np.mean(self.matrix)

    def median(self):
        return np.median(self.matrix)

    def corrcoef(self):
        return np.corrcoef(self.matrix)

    def var(self):
        return np.var(self.matrix)

    def std(self):
        return np.std(self.matrix)

    def count_greater_than_mean(self):
        mean = self.mean()
        count = np.sum(self.matrix > mean)
        return count

    def std_of_values_greater_than_mean(self):
        mean = self.mean()
        values = self.matrix[self.matrix > mean]
        std1 = np.std(values)
        std2 = np.sqrt(np.mean((values - np.mean(values)) ** 2))
        return round(std1, 2), round(std2, 2)

def task_5():
    npu = NumPUtils(5, 5)
    print("Matrix:\n", npu.matrix)
    print("Mean:", npu.mean())
    print("Median:", npu.median())
    print("Correlation Coefficient:\n", npu.corrcoef())
    print("Variance:", npu.var())
    print("Standard Deviation:", npu.std())
    print("Count of elements greater than mean:", npu.count_greater_than_mean())
    print("Standard Deviation of values greater than mean (two methods):", npu.std_of_values_greater_than_mean())
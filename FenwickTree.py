from random import randint
from itertools import accumulate


class BIT:
    """
    Creates a Binary Index Tree (Fenwick Tree)
    """
    def __init__(self, arr: [int]):
        """
        :param arr: Initializes and fills the fenwick array.
        """
        self.fenwick = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            self.update(i, arr[i])

    def sum(self, i: int) -> int:
        """
        Precondition: 0 <= i < len(fenwick)
        :param i: The index to get range sum from 0 to i
        :return: The sum of range from 0 to i.
        """
        i += 1
        total = 0
        while (i > 0):
            total += self.fenwick[i]
            i -= i & -i
        return total

    def update(self, i: int, amt: int) -> None:
        """
        Precondition: 0 <= i < len(fenwick)
        :param i: The index to update the original array
        :param amt: The amount to increase the index i of original array
        :return: None
        """
        i += 1
        while i < len(self.fenwick):
            self.fenwick[i] += amt
            i += i & -i

    def rangeSum(self, i: int, j: int) -> int:
        """
        Precondition: 0 <= i < len(fenwick), 0 <= j < len(fenwick) and i < j
        :param i: The start index of the given array. (Inclusive)
        :param j: The end index of the given array.   (Exclusive)
        :return: A sum of a range from the given array
        """
        return self.sum(j) - self.sum(i)

if __name__ == "__main__":
    size = 10
    arr = [randint(-100, 100) for i in range(size)]  # Takes an array of random integers numbers.
    bit = BIT(arr)  # Creates a Fenwick tree structure
    preSum = [*accumulate(arr)]

    
    # -------------------- Testing --------------------
    print("Original array:    ", arr)
    print("Prefix Sum array:  ", preSum)  # A prefix sum of arr to compare with BIT class to test
    # Sum from Fenwick Tree
    print("Fenwick Tree array:", "[", end="")
    for i in range(size - 1):
        print(bit.sum(i), end=", ")
    print(bit.sum(size - 1), "]", sep="")
    print("Sum of 2nd quarter of array using prefix array:     ",preSum[size // 2] - preSum[size // 4])  # Range sum using (final - start).
    print("Sum of 2nd quarter of array using Binary Index Tree:",bit.rangeSum(size // 4, size // 2))  # Range sum using rangeSum method.

from sys import maxsize


class SegmentTree:

    def __init__(self, arr: list, func):
        """
        :param arr: The arryay to make the segment tree for.
        :param func: The function to use to fill the segment tree with.
        """
        self.size = len(arr)
        self.func = func
        self.tree = [0] * self.size + arr
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def range_query(self, idx1: int, idx2: int, default: int) -> int:
        """
        :param idx1: The start of the range query(inclusive)
        :param idx2: Then end of the range qurey (exclusive)
        :param default: The default value to start the query from. (Depends on the function)
        :return: The query result.
        """
        idx1 += self.size
        idx2 += self.size
        result = default

        while idx1 < idx2:
            if idx1 & 1:
                result = self.func(result, self.tree[idx1])
                idx1 += 1
            if idx2 & 1:
                idx2 -= 1
                result = self.func(result, self.tree[idx2])
            idx1 //= 2
            idx2 //= 2

        return result

    def update(self, idx: int, val: int) -> None:
        """
        :param idx: The index to update the original array with.
        :param val: The new value of the tree at idx
        """
        idx += self.size
        self.tree[idx] = val

        while idx > 1:
            idx //= 2
            self.tree[idx] = self.func(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def __repr__(self):
        return str(self.tree)


if __name__ == "__main__":
    arr = [6, 10, 5, 2, 7, 1, 0, 9]
    segTree = SegmentTree(arr, max)  # initilize segTree to [0,10,10,9,10,5,7,9,6,10,5,2,7,1,0,9]
    print("Original Array:", arr)
    print("Segment Tree:  ", segTree, end="\n\n")
    arr[5] = 8
    segTree.update(5, 8)
    print("Updated index 5 to value 8")
    print("Original Array:", arr)
    print("Segment Tree:  ", segTree, end="\n\n")  # update segTree to [0,10,10,9,10,5,8,9,6,10,5,2,7,8,0,9]
    print("Query 7-8:", segTree.range_query(len(arr) - 1, len(arr), -maxsize))  # Value of 9
    print("Query 7-8:", segTree.range_query(0, len(arr), -maxsize))  # Value of 10
    print("Query 7-8:", segTree.range_query(len(arr) // 2, len(arr) - 1, -maxsize))  # Value of 8

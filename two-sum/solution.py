from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.binary_scan(nums, target)

    def binary_scan(self, nums: List[int], target: int) -> List[int]:
        """Tends to do better in memory and is comparable in time.
        """
        sorted_map = sorted(range(len(nums)), key=lambda x: nums[x])
        ii, jj = 0, len(nums) - 1
        while True:
            delta = target - (nums[sorted_map[ii]] + nums[sorted_map[jj]])
            if delta < 0:
                jj -= 1
            elif delta > 0:
                ii += 1
            else:
                return [sorted_map[ii], sorted_map[jj]]

    def hash_map(self, nums: List[int], target: int) -> List[int]:
        """Does a little better in time, but worse in memory.
        """
        delta_map = {}
        for ii, value in enumerate(nums):
            other_index = delta_map.get(value)
            if other_index is not None:
                return [ii, other_index]
            delta_map[target - value] = ii


if __name__ == '__main__':
    examples = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
    ]
    for args, result in examples:
        assert Solution().twoSum(*args) == result

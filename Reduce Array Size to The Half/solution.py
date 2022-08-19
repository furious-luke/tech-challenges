from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        total = 0
        for ii, (_, count) in enumerate(counts.most_common()):
            total += count
            if total >= len(arr) // 2:
                return ii + 1
        return len(arr)


if __name__ == '__main__':
    test_cases = [
        ([3, 3, 3, 3, 5, 5, 5, 2, 2, 7], 2),
        ([7, 7, 7, 7, 7, 7], 1),
    ]
    for arr, result in test_cases:
        assert Solution().minSetSize(arr) == result

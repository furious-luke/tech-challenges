from random import randint
from bisect import bisect_left
from typing import List, Tuple


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        aa = nums1 if len(nums1) < len(nums2) else nums2
        bb = nums2 if len(nums1) < len(nums2) else nums1
        if not aa:
            return calc_median(bb)[1]
        while len(aa) > 2:
            ai, am = calc_median(aa)
            bi, bm = calc_median(bb)
            if am == bm:
                return am
            elif am < bm:
                a_to_del = ai
                b_to_del = len(bb) - bi - 1 - (1 if is_even(bb) else 0)
                to_del = min(a_to_del, b_to_del)
                aa = aa[to_del:]
                bb = bb[:-to_del]
            else:
                a_to_del = len(aa) - ai - 1 - (1 if is_even(aa) else 0)
                b_to_del = bi
                to_del = min(a_to_del, b_to_del)
                aa = aa[:-to_del]
                bb = bb[to_del:]
            aa, bb = (aa, bb) if len(aa) < len(bb) else (bb, aa)
        for ae in aa:
            bi = bisect_left(bb, ae)
            bb = bb[:bi] + [ae] + bb[bi:]
        _, bm = calc_median(bb)
        return bm


def calc_median(nums: List[int]) -> Tuple[int, float]:
    mid = len(nums) // 2
    if is_even(nums):
        return mid - 1, 0.5 * (nums[mid - 1] + nums[mid])
    else:
        return mid, nums[mid]


def is_even(array):
    return len(array) % 2 == 0


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 3], [4, 5, 6]),
        ([1], []),
        ([], [1]),
        ([1, 3], [2]),
        ([1, 10000], [2]),
        ([10, 20], [5]),
        ([10, 20], [25]),
        ([1, 2], [3, 4]),
        ([-2, -1], [-5]),
        ([1, 1, 1, 1], [1, 1, 1]),
        ([1, 2, 2], [1, 2, 3]),
        ([1, 3, 3, 5, 5, 9, 9], [0, 5, 5, 6, 8, 8, 9, 9]),
        ([0, 3, 6, 6, 7], [0, 3, 5, 6, 8, 8]),
        ([1, 1, 3, 5, 6, 6], [2, 2, 3, 3, 4, 5, 5, 9, 9]),
        ([1, 4, 5, 5, 5, 7], [1, 2, 3, 3, 8, 10]),
        ([3, 4, 6, 7, 10, 10], [0, 1, 3, 5, 8, 8, 9, 10]),
        ([0, 0, 0, 1, 6, 6, 7, 8, 9, 9], [1, 1, 2, 4, 5, 7]),
    ]
    for nums1, nums2 in test_cases:
        _, real_med = calc_median(sorted(nums1 + nums2))
        med = Solution().findMedianSortedArrays(nums1, nums2)
        print(nums1, nums2, med, real_med)
        assert real_med == med
    for ii in range(200):
        print(ii)
        nums1 = list(sorted(randint(0, 100000) for _ in range(randint(5, 1000))))
        nums2 = list(sorted(randint(0, 100000) for _ in range(randint(5, 1000))))
        _, real_med = calc_median(sorted(nums1 + nums2))
        med = Solution().findMedianSortedArrays(nums1, nums2)
        try:
            assert real_med == med
        except AssertionError:
            print('ERROR')
            print(real_med, med)
            print(nums1)
            print(nums2)
            raise

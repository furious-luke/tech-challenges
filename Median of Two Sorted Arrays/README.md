# Median of Two Sorted Arrays

https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively,
return *the median* of the two sorted arrays. The overall run time complexity
should be `O(log (m+n))`.

## Discussion

This was surprisingly tricky; depending on the approach there are a lot of edge
cases to worry about.

An observation about the solution: I think it's a good idea to consider
*invariant properties* of the desired solution. Then, ask how the problem could
be reduced in size while maintaining the invariants.

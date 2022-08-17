#include <stdlib.h>
#include <stdio.h>
#include <assert.h>

int comparator(const int* a, const int* b, int* nums);

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
  int* result = (int*)malloc(2 * sizeof(int));
  int* const indices = (int*)malloc(numsSize * sizeof(int));
  for (int ii = 0; ii < numsSize; ++ii) {
    indices[ii] = ii;
  }
  // qsort_r behaves like standard qsort, but includes a contextual pointer.
  // This allows the comparator to reference the numbers in the array, but to
  // sort the indices.
  qsort_r(indices, numsSize, sizeof(int), comparator, nums);
  int ll = 0, rr = numsSize - 1;
  while (1) {
    const int delta = target - (nums[indices[ll]] + nums[indices[rr]]);
    if (delta < 0) {
      rr -= 1;
    }
    else if (delta > 0) {
      ll += 1;
    }
    else {
      result[0] = indices[ll];
      result[1] = indices[rr];
      *returnSize = 2;
      free(indices);
      return result;
    }
  };
}

int comparator(const int* a, const int* b, int* nums) {
  return nums[*a] - nums[*b];
}

int main(int argc, char* argv[]) {
  int return_size;
  int* result;
  {
    int nums[] = {2, 7, 11, 15};
    int target = 9;
    result = twoSum(nums, 4, target, &return_size);
    printf("%d, %d\n", result[0], result[1]);
    assert(nums[result[0]] + nums[result[1]] == target);
  }
  {
    int nums[] = {-1, -2, -3, -4, -5};
    int target = -8;
    result = twoSum(nums, 5, target, &return_size);
    printf("%d, %d\n", result[0], result[1]);
    assert(nums[result[0]] + nums[result[1]] == target);
  }
  return 0;
}

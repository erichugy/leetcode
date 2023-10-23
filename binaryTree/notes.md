# Binary Search

## General Algorithm
### Assumptions
- Array is sorted
- All unique values
- All comparable values

## Complexity Analysis (for all)
Let (n) be the size of the input array nums.

Time complexity: ```O(log⁡ n)```

- ```nums``` is divided into half each time. In the worst-case scenario, we need to cut nums until the range has no element, and it takes logarithmic time to reach this break condition.

Space complexity: ```O(1)```
- During the loop, we only need to record three indexes, left, right, and mid, they take constant space.

### 1 - Find the element

```
def binarySearch:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + right//2

        if target = arr[mid]:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else
            left = mid + 1
    return -1
```

### 2 - Find the place where you can place the element (using upper bound)

1) Initialize the boundaries of the search space as left = 0 and right = nums.size (Note that the maximum insert position can be nums.size)
2) If there are elements in the range [left, right], we find the middle index mid = (left + right) / 2 and compare the middle value nums[mid] with target:
    - If nums[mid] <= target, let left = mid + 1 and repeat step 2.
    - If nums[mid] > target, let right = mid and repeat step 2.
3) We finish the loop and left stands for the insert position:
    - If left > 0 and nums[left - 1] = target, return left - 1.
Otherwise, return -1.
```
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Set the left and right boundaries
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid

        if left > 0 and nums[left - 1] == target:
            return left - 1
        else:
            return -1
```
### 3 - Same thing as two but with Lower Bound (so right side)

## Use Cases
- Finding an element in a sorted array
    - Key Example Problems:
        - 35
- Finding where to place an element
    - 
    -
- Finding the

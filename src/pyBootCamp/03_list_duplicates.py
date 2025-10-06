"""This module provides a function to find a non-duplicate number in a list.
   The list is expected to contain integers \
   where every integer except one appears twice.
   Only one integer appears once in the list others appear twice.
   Example: [1, 2, 3, 2, 1] -> 3
   Example: [4, 5, 6, 5, 4, 7, 6] -> 7
   Example: [-1, -2, -3, -2, -1] -> -3
   Example: [-2, 1, -2, 3, 1] -> 3
"""
from typing import List


def find_non_duplicate(nums:List[int]) -> int:
  """Finds the non-duplicate number in a list 
     where every other number appears twice.


  Args:
      nums (List[int]): A list of integers
                        where every integer except one appears twice.
  Returns:
      int: The non-duplicate integer from the list.
  """
  result = 0
  for num in nums:
    result ^= num
  return result


if __name__ == "__main__":
  test_list = [4, 5, 6, 5, 4, 7, 6]
  print(f"The non-duplicate number in the list {test_list}",
        f"is {find_non_duplicate(test_list)}")
  test_list = [-2, 1, -2, 3, 1]
  print(f"The non-duplicate number in the list {test_list}",
        f"is {find_non_duplicate(test_list)}")

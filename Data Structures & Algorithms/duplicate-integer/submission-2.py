class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Your exact logic, just indented inside LeetCode's function:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

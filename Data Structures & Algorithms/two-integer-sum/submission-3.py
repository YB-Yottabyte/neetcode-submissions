class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums: [1, 2, 3, 3]; target = 3
        mem1 = {}

        """
        nums: [1, 2, 3]
        enumerate: gives index and value
        i = 0, num = 1, so you mem1 = i
        """
        for i, num in enumerate(nums):
            # 1 - 0, 2 - 1, 3 - 2, 3 - 3
            complement = target - num
            if complement in mem1:
                return [mem1[complement], i]
            mem1[num] = i
        return False
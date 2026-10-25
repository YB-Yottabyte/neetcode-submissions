class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 3 4 5 6
        for i in range(len(nums)):
            # 4 5 6
            for j in range(i + 1, len(nums)):
                # 3 + 4, 3 + 5, 3 + 6
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
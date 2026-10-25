class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory = []

        for i in nums:
            # duplicat
            if i in memory:
                return True
            else:
                # remember current value
                memory.append(i)
        return False
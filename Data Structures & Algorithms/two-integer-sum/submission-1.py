class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            numsi = nums[i]
            nums[i] = None
            if target-numsi in nums:
                x = i
                y = nums.index(target-numsi)
                break;
        return [x, y]
        
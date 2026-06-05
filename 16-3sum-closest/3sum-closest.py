class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closes = float('inf')
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i > 0:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < abs(closes - target):
                    closes = s
                
                if s == target:
                    return s
                
                elif s < target:
                    left +=1
                else:
                    right -=1

        return closes
            

            
            
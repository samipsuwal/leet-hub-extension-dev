class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort() #nlog(n)
        
        def helper(nums, i, target):
            j = len(nums)-1
            sum=0
            while(i<j):
                if nums[i] + nums[j] < target:
                    sum+= j-i
                    i+=1
                else:
                    j-=1
            return sum
        
        
        sum =0
        for i in range(n):
            sum += helper(nums, i+1, target-nums[i])
            
            
        
        
        return sum
        
        
                    
        return ans
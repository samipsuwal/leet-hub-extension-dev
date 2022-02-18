class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n ==1:
            return 1
    
        i = 1
        j = 0

        lastInserted = nums[0]

        endOfDups =False
        count = 0

        while i<n:
            if j >= n:
                if not endOfDups:
                    endOfDups =True
                    count = i

                nums[i]="_"
                i+=1

                continue

            if nums[j]>lastInserted:
                lastInserted = nums[j]
                nums[i] = lastInserted
                i+=1
                count = i
            else:
                j+=1



        return count

        
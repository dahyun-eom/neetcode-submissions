class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(list)
        nums.sort()
        temp = nums[0]
        count = 0
        for num in nums:
            if num != temp:
                res[count].append(temp)
                temp = num
                count = 1
            else:
                count+=1
                temp = num
        res[count].append(temp)
        

        sortedCount = sorted(res.keys(), reverse=True)  #내림차순
        return_list = []

        for i in range(k):
            if len(return_list)<k:
                for j in res[sortedCount[i]]:
                    return_list.append(j)
        return return_list


            
            

        #dictionary key: frequency, value: list
        #1. dict key: num, value: value in nums
        #2. The test cases are generated such that the answer is always unique.


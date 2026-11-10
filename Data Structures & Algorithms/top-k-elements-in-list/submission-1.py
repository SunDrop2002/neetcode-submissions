class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  0   1  2  3
        # [[],[],[],[]]
        # create dictionary and insert key,values as num,freq
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        # create bucket
        buckets = [[] for _ in range(len(nums)+1)]

        # append freq values in bucket
        for n,c in freq.items():
            buckets[c].append(n)  

        #find top k element and return the list
        result = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                result.append(num)
            
                if len(result) == k:
                    return result

        return result


        


        
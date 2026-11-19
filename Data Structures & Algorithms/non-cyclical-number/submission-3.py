class Solution:
    def isHappy(self, n: int) -> bool:
        num = n
        square_map = set()      
        while True:
            digits = [int(d) for d in str(num)]
            sqr_sum = sum([n ** 2 for n in digits])
            
            if sqr_sum == 1:
                return True
            
            num = sqr_sum

            if num in square_map: 
                return False
            
            square_map.add(num)

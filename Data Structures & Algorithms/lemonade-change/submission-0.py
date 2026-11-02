class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0

        for i in bills:
            if i == 5:
                five += 1

            elif i == 10:
                if five < 1:
                    return False
                
                ten += 1
                five -= 1

            else:
                if five < 1:
                    return False

                if ten < 1:
                    if five < 3:
                        return False

                    five -= 3

                else:
                    ten -= 1
                    five -= 1

        return True
                
                
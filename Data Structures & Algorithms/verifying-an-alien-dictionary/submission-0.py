class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        adict = {c:i for i,c in enumerate(order)}

        for i in range(len(words)-1):
            
            m = 0
            w1 = words[i]
            w2 = words[i+1]
            while m < len(w1) and m < len(w2):
                if adict[w1[m]] < adict[w2[m]]:
                    break

                elif adict[w1[m]] > adict[w2[m]]:
                    return False
                
                else:
                    m += 1

            if m == min(len(w1), len(w2)) and len(w1) > len(w2):
                return False

        return True
            
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        i = 0
        j = len(people) - 1
        boats = 0
        while i <= j:
            summ = people[i] + people[j]

            if summ > limit:
                j -= 1
                boats += 1
            
            else:
                i += 1
                j -= 1
                boats += 1



        return boats
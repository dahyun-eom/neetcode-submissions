class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boat_num = 0
        people.sort(reverse=True)
        head = 0
        end = len(people) -1
        a = 0


        while head<=end:
            if head == end:
                a +=1
                break

            if people[head] + people[end] <= limit:
                boat_num += 1
                head += 1
                end -= 1
            else:
                head += 1
                

        people_one = len(people) - (boat_num*2)
        return people_one + boat_num
        
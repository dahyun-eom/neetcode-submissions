class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        difference = [abs(num - x) for num in arr]
        start = difference.index(min(difference))
        left = start - 1
        right = start + 1
        answer = [arr[start]]
        acc = 1

        while acc < k:
            if left < 0:
                answer.append(arr[right])
                right += 1
            elif right >= len(arr):
                answer.append(arr[left])
                left -= 1
            elif difference[left] <= difference[right]:  #tie
                answer.append(arr[left])
                left -= 1
            else:
                answer.append(arr[right])
                right += 1
            acc += 1
        # answer.sort() #use slice instead
        return arr[left+1: right]
        return answer
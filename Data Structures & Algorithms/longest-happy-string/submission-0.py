class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""

        maxHeap = [(a, "a"), (b, "b"), (c, "c")]
        heapq.heapify_max(maxHeap)

        temp = None
        while maxHeap or temp:
            if not maxHeap and temp:
                return res

            cnt, char = heapq.heappop_max(maxHeap)

            if cnt == 0:
                continue
    
            res += char
            cnt -= 1

            if temp:
                heapq.heappush_max(maxHeap, temp)
                temp = None
            
            if len(res) >= 2 and res[-1] == res[-2]:
                temp = (cnt, char)
            else:
                heapq.heappush_max(maxHeap, (cnt, char))
        
        return res

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        selected = []
        last_poped_index = -1
        for index, num in enumerate(arr):
            if len(selected) < k or abs(num - x) < selected[0][0]:
                heapq.heappush_max(selected, (abs(num - x), index))
            if len(selected) == k + 1:
                heapq.heappop_max(selected)

        res = [arr[idx] for _, idx in selected]
        return sorted(res)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxCount = max(count.values())
        
        maxCountTasks = sum(1 for v in count.values() if v == maxCount)

        intervals = (maxCount-1) * (n + 1) + maxCountTasks

        return max(intervals, len(tasks))
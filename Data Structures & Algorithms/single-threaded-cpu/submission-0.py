class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available_tasks = [task + [i] for i, task in enumerate(tasks)]
        queued_tasks = []

        heapq.heapify(available_tasks)

        current_time = 0
        order = []
        while available_tasks or queued_tasks:
            if not queued_tasks and current_time < available_tasks[0][0]:
                current_time = available_tasks[0][0]
            while available_tasks and current_time >= available_tasks[0][0]:
                enqueue_time, processing_time, index = heapq.heappop(available_tasks)
                heapq.heappush(queued_tasks, [processing_time, index])
            
            curr_proessing_time, curr_index = heapq.heappop(queued_tasks)
            current_time += curr_proessing_time
            order.append(curr_index)
        
        return order    
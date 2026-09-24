import heapq
jobs = []
heapq.heappush(jobs,(-3,"Job A"))
heapq.heappush(jobs,(-5,"Job B"))
heapq.heappush(jobs,(-1,"Job C"))
heapq.heappush(jobs,(-4,"Job D"))
print("Jobs in heap order")
for priority, job in jobs:
    print("Processing : ",job,"Priority : ", -priority)
print("\nHighest priority job : ",jobs[0][1])
print("Priority : ", -jobs[0][0])
priority,job = heapq.heappop(jobs)
print("\nProcessed job : ",job)
print("Priority : ", -priority)
print("\nRemaining jobs : ")
for priority, job in jobs:
    print(job,"Priority : ", -priority)

import heapq

jobs = []

while True:
    print("\n--- Priority Queue Menu ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        job = input("Enter job name: ")
        priority = int(input("Enter priority: "))

        heapq.heappush(jobs, (-priority, job))
        print("Job inserted successfully.")

    elif choice == 2:
        if len(jobs) == 0:
            print("No jobs available.")
        else:
            priority, job = heapq.heappop(jobs)
            print("\nDeleted job:", job)
            print("Priority:", -priority)

    elif choice == 3:
        if len(jobs) == 0:
            print("No jobs available.")
        else:
            priority, job = jobs[0]
            print("\nHighest priority job:", job)
            print("Priority:", -priority)

    elif choice == 4:
        if len(jobs) == 0:
            print("No jobs available.")
        else:
            print("\nJobs in heap order:")
            for priority, job in jobs:
                print("Job:", job, "Priority:", -priority)

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")

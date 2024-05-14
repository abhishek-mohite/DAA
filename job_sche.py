import random
JOBS=5

def job_schedule(job_ids,deadlines,profits):

    jobs=list(zip(job_ids,deadlines,profits))

    jobs.sort(key=lambda x: x[2],reverse=True)

    max_deadline=max(deadlines)
    schedule=[None]*max_deadline

    total_profit=0
    for job_id,deadline,profit in jobs:
        for i in range(deadline-1,-1,-1):
            if schedule[i]==None:
                schedule[i]=job_id
                total_profit+=profit
                break
    schedule=[job for job in schedule if job is not None]

    return total_profit,schedule

job_ids=[i for i in range(1,JOBS+1)]
deadlines=[random.randint(1,JOBS+1) for i in range(JOBS) ]
profits=[random.randint(1,50) for i in range(JOBS)]

print(f"job_ids:{job_ids}")
print(f"deadlines:{deadlines}")
print(f"profits:{profits}")

total_profit,schedule=job_schedule(job_ids,deadlines,profits)

print(f"Total Profit:{total_profit}\nSchedule:{schedule}")

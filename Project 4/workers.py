from itertools import permutations


class Worker:
    def __init__(self):
        self.tasks = []
        self.time = 0
        self.tot_time = 0
        self.working = False


def order_tasks(tasks: list, workers: int) -> float:
    tasks = [int(i*100) for i in tasks]
    workers = [Worker() for _ in range(workers)]
    i = 0
    while i < 5000:
        i += 1
        for worker in workers:
            if not worker.working:
                try:
                    worker.tasks.append(tasks.pop(0))
                except IndexError:
                    continue
                worker.working = True
            else:
                worker.time += 1
                if worker.time == worker.tasks[-1]:
                    worker.tot_time += worker.time
                    worker.time = 0
                    worker.working = False
    return max(workers, key=lambda worker: worker.tot_time).tot_time/100


def best_order_tasks(input_tasks: list, n_workers: int) -> float:
    input_tasks = [int(i*100) for i in input_tasks]
    min_time = [2**16, input_tasks]
    for tasks in permutations(input_tasks):
        tasks = list(tasks)
        copy = tasks.copy()
        workers = [Worker() for _ in range(n_workers)]
        i = 0
        while i <= 5000:
            i += 1
            for worker in workers:
                if not worker.working:
                    try:
                        worker.tasks.append(tasks.pop(0))
                    except IndexError:
                        continue
                    worker.working = True
                else:
                    worker.time += 1
                    if worker.time == worker.tasks[-1]:
                        worker.tot_time += worker.time
                        worker.time = 0
                        worker.working = False
        min_time = min([min_time, [max(
            workers, key=lambda worker: worker.tot_time).tot_time, copy]], key=lambda x: x[0])
    return min_time[0]/100, min_time[1]


print(order_tasks([1, 2], 1))  # Output: 3
print(order_tasks([1, 2], 2))  # Output: 2
print(order_tasks([1, 2], 3))  # Output: 2
print(order_tasks([1, 2, 3, 4], 2))  # Output: 6
print(order_tasks([4, 3, 2, 1], 2))  # Output: 5
print(order_tasks([1, 2, 3, 4], 3))  # Output: 5
print(order_tasks([4, 3, 2, 1], 3))  # Output: 4
print()
print(order_tasks([7.51, 7.57, 7.23], 2))  # Output: 14.74
print(order_tasks([3.25, 0.46, 0.03, 9.98, 5.49], 2))  # Output: 10.47
print(order_tasks([7.44, 2.61, 5.32, 3.31, 3.3, 4.55, 1.86], 2))  # Output: 15.3
print(order_tasks([0.38, 4.01, 9.58, 6.47, 9.44], 3))  # Output: 13.45
print(order_tasks([8.33, 6.37, 0.14], 1))  # Output: 14.84

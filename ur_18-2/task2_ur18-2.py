class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_

        self.name = name

        self.company = company

        self._workers = []

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, worker):
        if not isinstance(worker, Worker):
            raise ValueError('Worker must be a class Worker')
        if worker not in self._workers:
            self._workers.append(worker)
            worker.boss = self


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_

        self.name = name

        self.company = company

        self._boss = None

        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss: Boss):
        if not isinstance(boss, Boss):
            raise ValueError('Boss must be a Boss instance')
        if self._boss is not None:
            self._boss.workers.remove(self)
        self._boss = boss
        boss.workers.append(self)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

boss1 = Boss(1, "Boss One", "Company A")
boss2 = Boss(2, "Boss Two", "Company B")

worker1 = Worker(101, "Worker One", "Company A", boss1)
worker2 = Worker(102, "Worker Two", "Company A", boss1)

print(boss1.workers)  # ->  [worker one, worker two]

# Reassign workers
worker2.boss = boss2
print(boss1.workers)  # ->  [worker one]
print(boss2.workers)  # ->  [worker two]

worker3 = Worker(103, "Worker Three", "Company B", boss2)
print(boss2.workers)  # -> [worker two, worker three]

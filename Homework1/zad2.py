import string

class Worker:
    number: int
    name: string
    age: int
    salary: int

    def __init__(self, number, name, year_of_birth, salary):
        self.number = number
        self.name = name
        self.age = 2022 - year_of_birth
        self.salary = salary

workers = [
    Worker(1, "Adam", 1983, 1500),
    Worker(2, "Anna", 1981, 1700),
    Worker(3, "Błażej", 1990, 1800),
    Worker(4, "Beata", 1992, 1600),
    Worker(5, "Czesław", 1980, 2000),
    Worker(6, "Cecylia", 1983, 2100),
    Worker(7, "Daniel", 1976, 1900),
]

# Obliczanie średniej pensji
def calc_avg_salary(workers):
    if len(workers) == 0:
        return 0
    salary_sum = 0
    for worker in workers:
        salary_sum += worker.salary

    return salary_sum/len(workers)

print(calc_avg_salary(workers))

# Porównanie zarobków osób młodzszych niż 30 lat i starszych
younger_workers = []
older_workers = []

for worker in workers:
    if worker.age < 30:
        younger_workers.append(worker)
    else:
        older_workers.append(worker)

print(calc_avg_salary(younger_workers))
print(calc_avg_salary(older_workers))

if calc_avg_salary(younger_workers) > calc_avg_salary(older_workers):
    print("Młodsi zarabiają więcej")
else:
    print("Starsi zarabiają więcej")

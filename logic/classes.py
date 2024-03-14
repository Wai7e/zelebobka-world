from random import randint

class Human:
    def __init__(self, name, lastname, age, height, weight, job, harm):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.height = height
        self.weight = weight
        self.job = job
        self.harm = harm

    def human_raise(self):
        self.age += 1
        if self.height <= 200:
            if self.age <= 20:
                self.height += randint(1, 5)
            else:
                if randint(1, 100) >= 97:
                    self.height += 1
        return self

    # def human_

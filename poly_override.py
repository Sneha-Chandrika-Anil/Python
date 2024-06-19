class Player:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}")

class Cricketer(Player):
    def __init__(self, name, age, team, role):
        super().__init__(name, age)
        self.team = team
        self.role = role

    def display(self):
        return super().display()
        print(f"Team: {self.team}")
        print(f"Role: {self.role}")

class Footballer(Player):
    def __init__(self, name, age, team):
        super().__init__(name, age)
        self.team = team

    def display(self):
        return super().display()
        print(f"Team: {self.team}")

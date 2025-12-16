class student:
    roll_no = 21
    def __init__(self,roll_no):
        self.roll_no = roll_no
    def learn(self):
        return "learning"
    def bunk(self):
        pass
saad = student(157)
print(saad.roll_no)
print(saad.learn()) 

class faculty:
    def teach(self):
        return "im teaching discipline to student"
prasad_sir1 = faculty()
print(prasad_sir1.teach())
print(prasad_sir1.discipline())



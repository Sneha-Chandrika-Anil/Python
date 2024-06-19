class Sem3 :
    def __init__(self,name):
        self.name = name
    def class_duties(self):
        print("Attendence")
    def plcmt_duties(self):
        print("Discipline")

classRep = Sem3("Sivanand")
placementRep = Sem3("Gracen")
print(classRep.name)
classRep.class_duties()
print(placementRep.name)
classRep.plcmt_duties()

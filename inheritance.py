class McaCourse:
    def __init__(self,name,code):
        self.name = name
        self.code = code

    def courseDetails(self):
        print("Course code: "+self.code+"\nCourse name: "+self.name)

class Subject(McaCourse):
    def __init__(self,name,code,sem):
        super().__init__(name,code)
        self.sem = sem

    def fullDetails(self):
        print("Course code: "+self.code+"\nCourse name: "+self.name+"\nSemester: "+self.sem)

obj = Subject("Data Analytics Using Python","MCA305","3")
obj.fullDetails()
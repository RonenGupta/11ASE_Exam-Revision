class Person:
    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName

    def printFullName(self):
        return self.firstName + ' ' +  self.lastName

class Student(Person):
    def __init__(self, firstName: str, lastName: str, studentID: int, homeroom: str):
        super().__init__(firstName, lastName)
        self.studentID = studentID
        self.homeroom = homeroom

    def enrollClass(self, subject):
        subject.studentID.append(self.studentID)
        print(f"{self.printFullName()} has been enrolled with student ID: {self.studentID} in class: {subject.subjectName}!")

class Parent(Person):
    def __init__(self, firstName: str, lastName: str, occupation: str, alumni: bool):
        super().__init__(firstName, lastName)
        self.occupation = occupation
        self.alumni = alumni

class Subject():
    def __init__(self, subjectName):
        self.studentID = []
        self.subjectName = subjectName

    def printStudentList(self):
        for id in self.studentID:
            print(id)
        
stdt1 = Student('Ronen', 'Gupta', 9999, 'Class A')
stdt2 = Student('Levin', 'Shao', 1000, 'Class A')
math = Subject('Math')
stdt1.enrollClass(math)
stdt2.enrollClass(math)
math.printStudentList()
#Arushi Chauhan 2016019 
class Student(object):
    def __init__(self,RollNo,FirstName,LastName,Program,CGPA):
        self.RollNo=RollNo
        self.FirstName=FirstName
        self.LastName=LastName
        self.Program=Program
        self.CGPA=CGPA
    def comes_before(self,other):
        yr1=int(self.RollNo[:4])
        yr2=int(other.RollNo[:4])
        c1=self.Program
        c2=other.Program
        p1=float(self.CGPA)
        p2=float(other.CGPA)
        if yr1<yr2:
            return True
        elif yr1==yr2:
            if c1<c2:
                return True
            elif c1==c2:
                if p1>p2:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

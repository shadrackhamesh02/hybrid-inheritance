# Hybrid inheritance

class university :
    def detials1(self):
        print('THE UNIVERSITY NAME : ANNA UNIVERSITY')
class course(university):
    def detials2(self):
        print('THE COURSE NAME : B.E')
class branch(university):
    def detials3(self):
        print('THE BRANCH NAME : CSE')
class student(course,branch):
    def detials4(self):
        print('THE STUDENT NAME : SHADRACK HAMESH S')       
ob1 = student()
ob1.detials4()
ob1.detials2()
ob1.detials3()
ob1.detials1()
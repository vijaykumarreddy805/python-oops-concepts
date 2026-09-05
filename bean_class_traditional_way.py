class CMS: #bean class

    def __init__(self,marks,attendence,password):
        self.__marks = marks 
        self.__attendence = attendence
        self.__password = password

    def get_marks(self):
        return self.__marks

    def set_marks(self,marks):
        if marks >= 0 and marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    def get_attendence(self):
        return self.__attendence

    def set_attendence(self,attendence):
        if attendence >= 0 and attendence <= 100:
            self.__attendence = attendence
        else:
            print("Invalid Attendence")

    def get_pw(self):
        return self.__password

    def set_pw(self,password):
        if len(password) >= 8:
            self.__password = password
        else:
            print("Password length should be atleast 8 chars")

s1 = CMS(0,0,"")
print(s1.get_marks())
s1.set_marks(90)
print(s1.get_marks())
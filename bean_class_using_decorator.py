class cms:
    def __init__(self,password):
        self.__password = password
    @property
    def var(self):
        return self.__password
    @var.setter
    def var(self, password):
            if len(password)>=8:
                self.__password = password
                
            else:
                print("Password len should have atleast 8 chars")
s1 = cms("")
print(s1.var)
s1.var = "john1234566"
print(s1.var)
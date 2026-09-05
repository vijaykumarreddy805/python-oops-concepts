class cms:
    def __init__(self,password):
        self.__password = password
    def get_password(self):
        return self.__password
    def set_password(self, password):
        if len(password)>=8:
            self.__password = password
            
        else:
            print("Password len should have atleast 8 chars")
    var_pw = property(get_password,set_password)
s1 = cms("")
s1.var_pw = "john23"
print(s1.var_pw)
s1.var_pw = 'john12345'
print(s1.var_pw)

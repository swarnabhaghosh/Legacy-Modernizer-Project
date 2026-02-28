# class Login:
#     def login(self):
#         self.validateUser()
#         self.connectDB()

#     def validateUser(self):
#         print("Validating")

#     def connectDB(self):
#         print("Connecting")



class Login(object):  
    def login(self):  
        self._validate_user()    
        return self.__connectDB()     
    @staticmethod      
    def _validate_user():  
        print("Validating")  
    @classmethod    
    def __connectDB(cls):      
        print("Connecting")
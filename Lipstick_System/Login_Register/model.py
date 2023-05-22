from Lipstick_System import bcrypt
from Lipstick_System.mongo import users

class UserRegister():     
    def __init__(self, input):
        self.user_name = input['user_name']
        self.email = input['email']
        self.password = input['password']

        users.insert_one({
            "user_name": self.user_name,
            "email": self.email,
            "password": self.password_hash
        })        

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf8')

    def __repr__(self):
        return 'username:%s, email:%s' % (self.user_name, self.email)
    
class FormRegister():        
    def __init__(self, input):
        self.user_name = input['user_name']
        self.email = input['email']
        self.password = input['password']
        self.check_password = input['check_password']
        self.result = users.find_one({
            "email": self.email,
        })   

    def password_validation(self):
        if(self.password != self.check_password):
            return False
        return True
    
    def email_validation(self):
        if(self.result != None):
            return False
        return True

class FormLogin():        
    def __init__(self, input):
        self.email = input['email']
        self.password = input['password']
        self.result = users.find_one({
            "email": self.email,
        })   

    def check_password(self, password):
        return bcrypt.check_password_hash(password, self.password)
    
    def email_validation(self):
        if(self.result == None):
            return False
        return True    
    
    def password_validation(self):
        return self.check_password(self.result['password'])
    
    def getUserName(self):
        return self.result['user_name']
    
    def getEmail(self):
        return self.result['email']

class ResetPwd():        
    def __init__(self, input):
        self.email = input['email']
        self.password = input['password']
        self.check_password = input['check_password']
        self.password_hash = bcrypt.generate_password_hash(self.password).decode('utf8')

    def password_validation(self):
        if(self.password != self.check_password):
            return False
        return True
    
    def reset_password(self):        
        filter = { 'email': self.email }
        newvalues = { "$set": { 'password': self.password_hash } }

        users.update_one(filter, newvalues)



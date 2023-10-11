# your User class goes here
class User:
    # init is short for initalize
    species_type= "human" #class attribute
    def __init__(self, name, email_address, drivers_license_number="unknown"):# first argument passed into init is the class itself "self"
        self._name = name #these are all instance attributes
        self._email = email_address #instance attribute
        self._dln = drivers_license_number #instance attribute
        self._friends= 0
    @property #properties must be declared for getters
    def name(self):
        return self._name
    @property
    def email(self):
        return self._email
    @property
    def dln(self):
        return self._dln
    @property
    def friends(self):
        return self._friends
    # dundermethod is usually underscores before after, cannot be overwritten
    def __str__(self):
        # instead of printing a memory location it prins this string
        return f"{self.name}'s email is {self.email} and drivers liscense number is {self.dln}"
    @friends.setter #setter
    def set_friends(self, new_friends_number):
        if new_friends_number > 0:
            self._friends = new_friends_number
            

user_1= User("tom", "tom@myspace.com", 2003030)
user_2 = User("McLovin", "mclovin@hawaii.gov", 14787441)

# is using __str__ method
print(user_2)#print of the self will use the string method
# print(user_1)

import yaml



#Create a metaclass
class METAClass(type):
    def __new__(cls,name,bases,dct):
        #Get yaml data, or if none found use empty dict
        friends_yaml = dct.get("__friends_yaml__", {})
        #Loop through dat
        #Check for nested dict
        for key, value in friends_yaml.items():
            if isinstance(value, dict):
                #Create new class for nested dict
                nested_class=METAClass(key.capitalize(), (object, ), {'__friends_yaml__': value})
                dct[key] = nested_class()
            else:
                dct[key] = value
        
        return super().__new__(cls, name, bases, dct)
    
#Create class from metaclass

class YAMLInstance (metaclass = METAClass):
    def __init__(self, data):
        self.__friends_yaml__ = data
        #Loop through data
        #Create classes for nested key values
        for key, value in data.items():
            #Create 
            if isinstance(value, dict):
                setattr(self, key, YAMLInstance(value)) 
            else:
                setattr(self, key, value)
                

friends_yaml = """casual_friends: 
  friend_1: 
    name: 'Joe' 
    address: 
    street: 'Boundary Rd' 
    Number: 66 
  friend_2: 
    name: 'Anne' 
    mobile: 0275550011 
    address: 
    street: 'County St' 
    Number: 31 """

friends = yaml.safe_load(friends_yaml)


base =YAMLInstance(friends)
 
print(base.casual_friends.friend_1.name)
print(base.casual_friends.friend_2.street)
    

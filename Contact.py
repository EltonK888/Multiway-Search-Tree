class Contact():
    ''' This class constructs a structure to store people's contact information'''
    def __init__(self, phone, name):
        '''(Contact, str, str) -> NoneType
        constructs a contact by the given phone number
        and name.
        REQ: phone follows xxx-xxx-xxxx format'''
        self._phone = phone
        self._name = name
   
    def set_name(self, name): 
        '''(Contact, str) -> NoneType'''
        self._name = name 
    def set_phone(self, phone): 
        '''(Contact, str) -> NoneType'''
        self._phone = phone
    def get_name(self): 
        '''(Contact) -> str'''
        return self._name
    def get_phone(self): 
        '''(Contact) -> str'''
        return self._phone 

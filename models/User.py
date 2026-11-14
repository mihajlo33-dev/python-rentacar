# public, protected, private

# public = self.name -> public -> Ova varijabla moze da se pozove iz te klasae ili iz bilo kog drugog mesta
# protected = self._name_ -> protected -> Podatak moze se pozove iz te klase ili klasa koje nasledjuju
# private = self.__name -> private -> moze da se pozove samo iz svoje klase


import Db

class User(Db):

    def __init__(self):
        super().__init__()

    def set_age(self, age):
        if age < 18:
            raise ValueError("Godine moraju biti minimum 18")

        self.__age = age

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) <  3:
            raise ValueError("Ime mora imati minimum 3 karaktera")
        self.__name = name




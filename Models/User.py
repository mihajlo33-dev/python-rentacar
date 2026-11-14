# public, protected, private

# public = self.name -> public -> Ova varijabla moze da se pozove iz te klasae ili iz bilo kog drugog mesta
# protected = self._name_ -> protected -> Podatak moze se pozove iz te klase ili klasa koje nasledjuju
# private = self.__name -> private -> moze da se pozove samo iz svoje klase


import Db


class User(Db):

    def __init__(self):
        super().__init__()
        self.__age = None
        self.__name = None

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("Godine moraju biti minimum 18")

        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

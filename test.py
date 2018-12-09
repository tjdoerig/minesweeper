
class User:
    """Das ist ein Doc-String"""

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday  #yyyymmdd

    #Extract first and last names
    #name_pices = name.split(" ")
    #self.first_name = name_pices[0]
    #self.last_name = name_pices[-1]

    #def introduce_self(self):
     #   print(self.name)

User1 = User("Dave Bowman", 19900129)
User2 = User("Thomas Doerig", 29011990)


    #def age(self):
    #    today = datetime.date()
    #    yyyy = int(self.birthday[])


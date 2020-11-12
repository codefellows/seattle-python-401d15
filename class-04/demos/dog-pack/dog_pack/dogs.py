class Dog():
    def sleep(self):
            return "zzz"

    @staticmethod
    def get_characteristics():
        return "Plain old dog"

class Puggle(Dog):

    count = 0

    def __init__(self, name="unknown poochie"):
        self.name = name
        Puggle.count += 1


    def greet(self):
        return f"I am {self.name}. I am SO HAPPY to meet you!"


    @staticmethod
    def get_characteristics():
        return "Like a mini boxer"

    @classmethod
    def get_breed_count(cls):
        return cls.count


class Boxer(Dog):

    def __init__(self, name="unknown"):
        self.name = name

    def greet(self):
        return f"The name's {self.name}. Pleasure."


# only run this when running directly as a "script"
if __name__ == "__main__":
    print('hi there')
    boxer = Boxer()
    print(boxer)

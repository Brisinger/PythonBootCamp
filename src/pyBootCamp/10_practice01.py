# Class depicting a programmer
'''
    Programmer class
'''
class Programmer:
    Company = "Microsoft"
    def __init__(self, name, language) -> None:
        self.language = language
        self.name = name
    
    def __str__(self) -> str:
        members = [self.language, self.__class__.__name__, self.name]
        return '|'.join(members)

# Instances of Programmer class
harry = Programmer("Harry", "Python")
shubho = Programmer("Shubhojit", ".NET")
print(harry)
print(shubho)

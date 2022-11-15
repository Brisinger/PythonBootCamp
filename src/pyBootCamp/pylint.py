'''
Pylint Tutorial
'''

class Car:
    '''
    A class to represent a car

    ...

    Attributes
    ----------
    color : str
         color of the car

    Methods
    -------
    crash(car):
        sets the car's color to burnt after a crash.
    __str__():
        returns the string representation of Car object.
    '''
    def __init__(self, color) -> None:
        '''
        Constructs all the necessary attributes for the car object.

        Parameters
        ----------
            color : str
                 color of the car
        '''
        self.color = color

    @staticmethod
    def crash(car):
        '''
        Sets the color of a car to burnt after the car crashed.

        Parameters
        ----------
            car : car object, required
               car object that crashed.

        Returns
        -------
        None
        '''
        car.color = 'burnt'

    def __str__(self):
        '''
        returns the string representation of the car object.

        Returns
        -------
        str
        '''
        return self.color + " " + "car"

myCar = Car('blue')
Car.crash(myCar)
print(myCar)

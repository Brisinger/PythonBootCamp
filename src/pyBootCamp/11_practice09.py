# module to implement cooperative multiple inheritance.
# passing all required arguments along with keyword arguments and a keyword arguments dictionary.
# dispatching method calls from caller to callee ensuring argument patterns are matched.
# In the object class while dispatching the call using super the method is not found.
# Badly designed classes for cooperatively dispatching method calls along mutiple inheritance chain.


class Shape():
    """Class depicting a shape with a name.
    
    
    Attributes:
    -----------
        shapename (str): Name of the shape instance.

    Methods:
    -------
        draw(): Draws a shape by printing its name and dispatches the call to its parent in inheritance chain.
    """
    def __init__(self, _name, **kwargs) -> None:
        """Initialize the shape instance.
        

        Args:
        -----
            _name (str): Name of the shape.
            **kwargs (dict): Dictionary of keyword arguments.
            Each keyword argument in **kwargs required by the caller gets stripped-off.
            The method is dispatched to the callee in method resolution order with remaining arguments in **kwargs.
        """
        self.shapename = _name
        super().__init__(**kwargs)

    def draw(self) -> None:
        """Drawing by printing the shape name."""
        print('Drawing. Setting shape to:', self.shapename)
        return super().draw()


class ColoredShape(Shape):
    """Class depicting a shape with color and a name.
    
    
    Attributes:
    ----------
        color (str): Color of the shape instance.

    Methods:
    --------
        draw(): Draws the shape by printing its color and and dispatches the call to its parent in inheritance chain to print its name.
    """
    def __init__(self, _color, **kwargs) -> None:
        """Initialize the shape instance color.
        
        
        Args:
        -----
            _color: Color of the shape.
            **kwargs (dict): Dictionary of keyword arguments.
            Each keyword argument in **kwargs required by the caller gets stripped-off.
            The method is dispatched to the callee in method resolution order with remaining arguments in **kwargs.
        """
        self.color = _color
        super().__init__(**kwargs)

    def draw(self) -> None:
        """Drawing by printing the shape color."""
        print('Drawing. Setting color to:', self.color)
        return super().draw()


if __name__=="__main__":
    shape = ColoredShape(_color="Red", _name="Circle")
    shape.draw()

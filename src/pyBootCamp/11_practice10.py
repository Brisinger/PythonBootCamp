# Cooperative multiple inheritance with method arguments pattern ensured.
# Class designed with method of interest always defined in caller.
# Root class to handle method call to callee by caller.
# Root class checks if the method exists in callee before dispatching method call to callee.
# Good design for cooperative multiple inheritance with classes in dynamic execution environment.
# Adapter class to integrate with third-party Movable class that doesn't conform to cooperative multiple inheritance rules.
from movables import Movable


class Root:
    """Parent class.
    This class eats away any method dispatched by callers down the inheritance chain
    without dispatching it to the base object class at top of method resolution order.
    
    Prevents AttributeErrorException from being raised by callers dispatching method to callee with no such method defined.


    Methods:
    --------
        draw(): Draws a shape without dispatching the call any further up the inheritance chain using super.
    """
    def draw(self):
        """Eats up the draw method dispatched by caller subtype in inheritance chain."""
        # the delegation chain stops here
        assert not hasattr(super(), 'draw')


class Shape(Root):
    """Shape with a name.


    Attributes:
    -----------
        shapename (str): Name of the shape instance.

    Methods:
    --------
        draw(): Draws a shape by printing name of the shape instance.
    """
    def __init__(self, shapename, **kwds):
        """Initializes a shape instance with a name.
        

        Args:
        -----
            shapename (str): Name of the shape.
            **kwargs (dict): Dictionary of keyword arguments.
            Each keyword argument in **kwargs required by the caller gets stripped-off.
            The method is dispatched to the callee in method resolution order with remaining arguments in **kwargs.
        """
        self.shapename = shapename
        super().__init__(**kwds)

    def draw(self):
        """Drawing by printing the shape name."""
        print('Drawing.  Setting shape to:', self.shapename)
        super().draw()


class MovableAdapter(Root):
    """Adapter class.
    This class integrates with Movable class by composition.
    Follows the rules of cooperative multiple inheritance.


    Attributes:
    -----------
        movable (Movable): Movable class instance composed in adapter.
    
    Methods:
    --------
        draw(): Draws the shape by specifying the co-ordinates to start drawing 
        and dispatches the call to its parent in inheritance chain.
    """
    def __init__(self, x, y, **kwargs) -> None:
        """Initializing MovableAdapter instance.
        The adapter composes incompatible Movable class.
        Integrates with rules of cooperative multiple inheritance.

        
        Args:
        -----
            x (int): Position depicting x co-ordinate.
            y (int): Position depicting x co-ordinate.
            **kwargs (dict): Dictionary of keyword arguments.
            Each keyword argument in **kwargs required by the caller gets stripped-off.
            The method is dispatched to the callee in method resolution order with remaining arguments in **kwargs.
        """
        self.movable = Movable(x, y)
        return super().__init__(**kwargs)

    def draw(self):
        """Draws the shape specifying the position."""
        self.movable.draw()
        return super().draw()


class ColoredShape(Shape):
    """Shape with color and a name.
    
    
    Attributes:
    -----------
        color (str): Color of shape instance.

    Methods:
    --------
        draw(): Draws the shape by printing its color and dispatches the call to its parent in inheritance chain to print its name.
    """
    def __init__(self, color, **kwds):
        """Initializes the color with a name of shape instance.
        
        
        Attributes:
        -----------
            color (str): Color of the shape.
            **kwargs (dict): Dictionary of keyword arguments.
            Each keyword argument in **kwargs required by the caller gets stripped-off.
            The method is dispatched to the callee in method resolution order with remaining arguments in **kwargs.
        """
        self.color = color
        super().__init__(**kwds)

    def draw(self):
        """Drawing by printing the shape color."""
        print('Drawing. Setting color to:', self.color)
        super().draw()


class MovableColoredShape(ColoredShape, MovableAdapter):
    """Extends the ColoredShape instance by composing MovableAdapter.
    The draw method extends the color and shape by printing the 
    position of the co-ordinates for drawing the given shape. 
    """
    def __init__(self, **kwargs) -> None:
        """Initializes MovableColoredShape instance and its parent classes up the method resolution order.
        
        
        Attributes:
        -----------
            **kwargs (dict): Dictionary of keyword arguments. Each keyword argument in **kwargs required by the caller gets stripped-off. The method gets dispatched to the callee in method resolution order with remaining arguments in **kwargs.
        """
        print("Method resolution order of", super().__thisclass__, "is", super().__self_class__.__mro__)
        return super().__init__(**kwargs)


if __name__=="__main__":
    shape = ColoredShape(color="Blue", shapename="Square")
    shape.draw()

    movable_shape = MovableColoredShape(color="Red", shapename="Triangle", x=10, y=20)
    movable_shape.draw()
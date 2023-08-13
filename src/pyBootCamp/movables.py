# Implements Movable class that doesn't follow cooperative multiple inheritance techniques.


class Movable():
    """Movable class with co-ordinates to draw.
    
    
    Attributes:
    ----------
        x (int): Position depicting x co-ordinate.
        y (int): Position depicting y co-ordinate.
    
    Methods:
    --------
        draw(): Specifies x and y co-ordinates respectively for drawing.
    """
    def __init__(self, x, y) -> None:
        """Initializes the position for drawing a Movable instance.


        Args:
        -----
            x (int): Position depicting x co-ordinate.
            y (int): Position depicting y co-ordinate.
        """
        self.x = x
        self.y = y

    def draw(self) -> None:
        """Specifies the co-ordinates to draw a movable instance."""
        print('Drawing at position:', self.x, self.y)
# read-only data descriptor providing a constant integer value.


class Verbose_attribute():
    """A class representing read-only data descriptor.
    
    
    Returns:
    --------
        A constant integer value 43.
    """
    def __get__(self, instance, type=type(int)) -> int:
        """Fetches the value of descriptor.
        
        
        Args:
        ----
            instance (object): Descriptor instance.
            type (type): Type of object fetched by descriptor.

        Returns:
        --------
            A constant integer value 43.
        """
        print("accessing the attribute to get the value")
        return 43
    
    def __set__(self, instance, value: int) -> None:
        """Set the value for descriptor.
        
        
        Args:
        -----
            instance (object): Descriptor instance.
            value (int): Integer value to set the descriptor.
        """
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")
    
# module to explore super object.


class A:
    """Class used as base class.


    Attributes:
    ----------
        val (int): Integer class based attribute.

    Methods:
    --------
        __str__() : Instance overriding string method returning the name of the class.
    """
    # class attribute
    val = 10

    def __str__(self) -> str:
        """Returns the name of the class.


        Returns:
        -------
            qualified name of the class as string.
        """
        return self.__class__.__qualname__


class B(A):
    """Class deriving from A.
    
    
    Attributes:
    -----------
        val (int): Integer class based attribute.

    Methods:
    --------
        __str__() : Instance overriding string method returning the name of the class.
    """
    val = 2

    def __str__(self) -> str:
        """Returns the name of the class.


        Returns:
        --------
            The qualified name of the class as a string.
        """
        return self.__class__.__qualname__


class C(A):
    """Class deriving from A.
    
    
    Attributes:
    -----------
        val (int): Integer class based attribute.

    Methods:
    --------
        __str__() : Instance overriding string method returning the name of the class.
    """
    val = 1

    def __str__(self) -> str:
        """Returns the name of the class.


        Returns:
        --------
            The qualified name of the class as a string.
        """
        return self.__class__.__qualname__


class X(A):
    """Class deriving from A.
    
    
    Attributes:
    -----------
        val (int): Integer class based attribute.

    Methods:
    --------
        __str__() : Instance overriding string method returning the name of the class.
    """
    val = 1

    def __str__(self) -> str:
        """Returns the name of the class.


        Returns:
        --------
            The qualified name of the class as a string.
        """
        return self.__class__.__qualname__


class Y(X):
    """Class deriving from X.
    
    
    Attributes:
    -----------
        val (int): Integer class based attribute.

    Methods:
    --------
        __str__() : Instance overriding string method returning the name of the class.
    """
    val = 3

    def __str__(self) -> str:
        """Returns the name of the class.


        Returns:
        --------
            The qualified name of the class as a string.
        """
        return self.__class__.__qualname__


class Z(Y, X):
    """Class deriving from Y and X.
    
    
    Attributes:
    -----------
        val (int): Integer class based attribute.

    Methods:
    --------
        __str__() : Instance overriding string method returning the name of the class.
    """
    val = 5

    def __str__(self) -> str:
        """Returns the name of the class.


        Returns:
        --------
            The qualified name of the class as a string.
        """
        return self.__class__.__qualname__


class D(C, Z, B):
    """Class deriving from B and C.
    
    
    Attributes:
    -----------
        val (int): Integer class based attribute.
    """
    val = 5
     


if __name__=="__main__":
    a = A()
    b = B()
    c = C()
    d = D()
    print("Class:",d)
    print(f"Method resolution order: {D.__mro__}")
    print(f"Is object of {d} an instance of {a}: {isinstance(b, A)}")
    print(f"Is object of {d} a subtype of itself: {issubclass(type(d), D)}")

    _super = super(C, d)
    print(f"Type of _super is {_super}, method resolution order: {type(_super).__mro__}")
    print(f"The val attribute: {_super.val}")

    _super = super(D, d)
    print(f"Type of _super is {_super}, method resolution order: {type(_super).__mro__}")
    print(f"The val attribute: {_super.val}")

    _super = super(B, d)
    print(f"The type of _super is {_super.__thisclass__}, the object or type of super's second argument is {_super.__self__} and {_super.__self_class__}")

    _super = super(D)
    print(f"The type of _super is {_super.__thisclass__}, the object or type of super's second argument is {_super.__self__} and {_super.__self_class__}")
    
    D.parent = _super
    print(f"The type of _super is {d.parent.__thisclass__}, the object or type of super's second argument is {d.parent.__self__} and {d.parent.__self_class__}")
# module showcasing usage of descriptor attribute.
from descriptors import Verbose_attribute


class Foo():
    """Class containing a descriptor attribute.
    
    
    Attributes:
    ----------
        desc: Read-Only data descriptor as a class attribute.
    """
    desc = Verbose_attribute()


if __name__=="__main__":
    # instantiating foo class.
    foo = Foo()

    # accessing descriptor attribute.
    x = foo.desc
    print(x)

    # foo class dictionary.
    class_dict = Foo.__dict__
    print(f"{foo.__class__.__qualname__} dictionary lookup:",class_dict)

    # attempting to set descriptor.
    try:
        foo.desc = 0
    except AttributeError as attex:
        print(attex)


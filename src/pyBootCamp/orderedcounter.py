# Composing Counter class and Ordered dict class from collections module.
# Extends both the classs to provide the functionality of an OrderedCounter class.
from collections import Counter, OrderedDict


class OrderedCounter(Counter,OrderedDict):
    """Class composing Counter and OrderedDict.
    OrderedCounter is a counter that remembers the order in which elements are inserted into dictionary. 
    """
    def __repr__(self) -> str:
        """Represents OrderedCounter instance with class name and ordered dictionary of its instances."""
        return '%s(%r)' % (self.__class__.__name__,
                            OrderedDict(self))
    
    def __reduce__(self):
         return self.__class__, (OrderedDict(self),)


if __name__=="__main__":
    oc = OrderedCounter("abracadabra")
    print(oc)
    # adds to the counter value for given key instad of replacing it.
    oc.update(r=2)
    print(oc)

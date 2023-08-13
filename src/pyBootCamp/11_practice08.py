# extending built-in types using super object.
from typing import Any
from collections import OrderedDict
import logging


class LoggingDict(dict):
    """Class extending python dict.
    
    
    Methods:
    -------
        __setitem__(key, value): Logs the key and value then adds the key-value pair in dictionary.
        __getitem__(__key): Fetches and returns the value for given key in dictionary.
    """
    def __init__(self):
        self.logger = logging.getLogger(name=__file__)
        logging.basicConfig(level=logging.INFO)

    def __setitem__(self, key, value) -> None:
        """Setting the dictionary with key, value pair.
        
        Attr:
        -----
            key: Key of dictionary.
            value: Value for key in dictionary.   
        """
        self.logger.info("Setting to %s, %s, in %s" % (key, value, super().__thisclass__))
        super().__setitem__(key, value)

    def __getitem__(self, __key: Any) -> Any:
        """Fetches the value of given key from dictionary.
        
        
        Attr:
        -----
            __key: The key for lookup in the dictionary.

        Returns:
        --------
            Value associated with given key in dictionary.
        """
        self.logger.info("Fetching value in %s for key: %s" % (super().__thisclass__, __key))
        return super().__getitem__(__key)
    

class LoggingOD(LoggingDict, OrderedDict):
    """Logging ordered dictionary.
    
    
    Methods:
    --------
        __setitem__(key, value): Adds the key-value pair in ordered dictionary and logs its content.
    """
    def __init__(self) -> None:
        """Initialize the LoggingOD class with ordered dict."""
        super().__init__()
        self.logger.info(msg=f"Logged ordered dict in {super().__thisclass__}: {self}")
    
    def __setitem__(self, key, value) -> None:
        """Setting the ordered dictionary with key, value pair.


        Attr:
        -----
            key: Key of ordered dictionary.
            value: Value for key in ordered dictionary.   
        """
        super().__setitem__(key=key, value=value)
        self.logger.info(msg=f"Logged ordered dict in {super().__thisclass__}: {self}")


if __name__=="__main__":
    # logging dict key/value pairs.
    logging_dict = LoggingDict()
    logging_dict["apple"] = 2
    logging_dict["orange"] = 4
    print("No. of apples:", logging_dict["apple"])
    print("No. of oranges:", logging_dict["orange"])

    # logging ordered dict key/value pairs.
    logging_od = LoggingOD()
    logging_od["banana"] = 12
    print("No. of bananas:", logging_od["banana"])
    
    # updating dictionary in ordered manner.
    logging_od.update(logging_dict)
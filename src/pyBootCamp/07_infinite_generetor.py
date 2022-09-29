# Genrator function returning infiite iterator
def generator(first):
    def wrap(func):
        def seq():
            x = first
            while True:
                yield x
                x = func(x)
        return seq
    return wrap


print("\nDisplay items in list using infinite iterator")
for item in generator(0)(lambda x: x + 1)():
    print(item)
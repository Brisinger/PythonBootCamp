'''
Decorator function
'''
def timeit(func, *args, **kwargs):
  '''
    Returns a tuple containing execution time and value returned by callback.
  '''
  def wrapper(*args, **kwargs):
    import time
    start = time.perf_counter()
    result = func(*args, **kwargs)
    finish = time.perf_counter() - start
    return finish, result
  return wrapper

@timeit
def adder(nums):
  '''
  Returns sum of items in iterable
  '''
  return sum(nums)

print(adder(range(100)))
print(adder(range(10000)))
print(adder(range(20000009)))


def reverse_string(func):
  def wrapper(text):
    result = reversed(text)
    return ''.join(result)
  return wrapper

@reverse_string
def word_sample(text):
    pass

def pairSum(input, target):
    if input is not type(list) and len(input) == 0:
      return None
    placeholder = []
    result = []
    for index in range(0, len(input)):
      look_up = target - input[index]
      if (look_up not in placeholder) \
        and (input[index] not in placeholder) \
        and (look_up in input[index + 1 :]):
        result.append((input[index],look_up))
      placeholder.append(input[index])
    return result

reversedText = word_sample("Tuesday")
print(reversedText)
pairs = pairSum([1, 4, 3], 3)
print(pairs)



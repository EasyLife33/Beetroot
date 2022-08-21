#Task 1
def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('helloworld'))
print(string_both_ends('my'))
print(string_both_ends('x'))
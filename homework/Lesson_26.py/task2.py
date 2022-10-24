from Lesson_26 import Stack


def is_balanced(sequence) -> bool:
    match = {')': '(', ']': '[', '}': '{'}
    s = Stack([])
    for char in sequence:
        if char in '({[':
            s.push(char)
        if char in match:
            if match[char] == s.peek():
                s.pop()
            else: return False
    return True if s.is_empty() else False


print(is_balanced('[]'))
print(is_balanced('[1, 2, {3}, (), 4]'))
print(is_balanced('[], (]'))
print(is_balanced('((('))

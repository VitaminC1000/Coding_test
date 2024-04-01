def solution(my_string):
    aeiou = ['a', 'e', 'i', 'o', 'u']
    return ''.join([s for s in my_string if s not in aeiou])
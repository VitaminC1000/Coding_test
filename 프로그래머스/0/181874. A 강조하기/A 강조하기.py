def solution(myString):
    return ''.join([i.upper() if i == "a" or i == "A" else i.lower() for i in myString])
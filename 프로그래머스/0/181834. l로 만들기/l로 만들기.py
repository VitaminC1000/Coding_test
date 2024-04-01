def solution(myString):
    return ''.join(["l" if ord(s) < ord("l") else s for s in myString])
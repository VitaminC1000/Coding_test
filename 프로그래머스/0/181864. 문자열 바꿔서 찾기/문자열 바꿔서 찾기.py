def solution(myString, pat):
    newString = ''.join(['B' if s == "A" else "A" for s in myString])
    return 1 if pat in newString else 0
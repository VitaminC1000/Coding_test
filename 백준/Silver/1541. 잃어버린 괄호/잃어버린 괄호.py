def minimum(eq):
    st = ""
    eq_arr = []

    for idx, s in enumerate(eq):
        if s == "+" or s == "-":
            eq_arr.extend([str(int(st)), s])
            st = ""
        else:
            st += s
            if idx + 1 == len(eq):
                eq_arr.append(str(int(st)))

    eq_arr.insert(0, "(")
    eq_arr.append(")")

    answer = [s if s is not "-" else ")" + s + "(" for s in eq_arr]

    return eval(''.join(answer))

eq = input()

print(minimum(eq))
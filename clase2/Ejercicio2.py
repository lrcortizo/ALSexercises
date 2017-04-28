def evaluate_prefix(l):
    def is_operator(x):
        if x in ['+', '*', '-', '/']:
            return True
        else:
            return False
    i = 0
    opr = l[i]
    i+=1
    op1 = l[i]
    if is_operator(op1):
        op1 = evaluate_prefix(l[1:])
        del(l[1:3])
    i += 1
    op2 = l[i]
    if is_operator(op2):
        op2 = evaluate_prefix(l[2:])
        del(l[2:5])
    expr = str(op1) + str(opr) + str(op2)
    return eval(expr)

l = "+ 1 - 5 * 2 4".split()
print("Resultado: ", evaluate_prefix(l))
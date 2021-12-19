def operation(item):
    global input_
    op = ["+","-","*","/","^","c","="]
    for ope in op:
        if ope == "+" or "-" or "/" or "*" or "^":
            op_answer = input_ + str(item)
        elif ope == "=":
            return op_answer
        elif ope == "c":
            input_ = ""
            input_txt = ""

input_ = ""








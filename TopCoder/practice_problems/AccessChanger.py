class AccessChanger:
    def convert(self, program):
        result = []
        for code in program:
            check_arrow = check_comment = False
            temp = ""
            for i in range(len(code)):
                if (code[i] == "-"):
                    check_arrow = True
                    check_comment = False
                    temp += code[i]
                elif (check_arrow and code[i] == ">"):
                    check_arrow = check_comment = False
                    temp = temp[:-1] + "."
                elif (code[i] == "/"):
                    if check_comment:
                        temp = temp + code[i:]
                        break
                    else:
                        temp += code[i]
                        check_arrow = False
                        check_comment = True
                else:
                    temp += code[i]
                    check_arrow = check_comment = False
            result.append(temp)
        return tuple(result)


AC = AccessChanger()
print(AC.convert(["Test* t = new Test();", "t->a = 1;",
                  "t->b = 2;", "t->go(); // a=1, b=2 --> a=2, b=3"]))

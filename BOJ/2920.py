scale = input()
result = 0
if scale[0] == "1":
    if scale[2] == "2":
        if scale[4] == "3":
            if scale[6] == "4":
                if scale[8] == "5":
                    if scale[10] == "6":
                        if scale[12] == "7":
                            if scale[14] == "8":
                                result = 1
elif scale[0] == "8":
    if scale[2] == "7":
        if scale[4] == "6":
            if scale[6] == "5":
                if scale[8] == "4":
                    if scale[10] == "3":
                        if scale[12] == "2":
                            if scale[14] == "1":
                                result = 2
if result == 1:
    print("ascending")
elif result == 2:
    print("descending")
else:
    print("mixed")

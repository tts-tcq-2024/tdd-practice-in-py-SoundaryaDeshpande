import re

def add(var1): 
    if var1 == "" or var1 == "0":  #testcase1 and testcase2
        return 0
    delimiter = ','
    elif var1.startswith("//"):   #testcas5 and tescase6
        delimiter_check = re.match(r"//(.+)\n", var1)
        if delimiter_check:
            delimiter = delimiter_check.group(1)
            var1 = var1.replace(f"//{delimiter}\n", "", 1)
        #var1 = re.sub(f"[{delimiter}\n]", ",", var1)
        var2 = re.split(r"\n|,",var1)
        #var2 = [int(num) for num in var2 if num]
        result = sum(int(num) for num in var2 if num.strip().isdigit())
    else: #testcase3 and testcase4
        var2 = var1.split(',')
        Num1 = int(var2[0].strip())
        Num2 = int(var2[1].strip())
        if Num1 > 1000:
            Num1 = 0
        if Num2 > 1000:
            Num2 = 0
        result = Num1 + Num2
    
    return result

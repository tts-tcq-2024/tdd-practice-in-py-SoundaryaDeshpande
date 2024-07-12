import re

def add(var1): 
    if var1 == "" or var1 == "0":
        return 0
    delimiter = ','
    if var1.startswith("//"):
        delimiter = re.match(r"//(.+)\n", var1).group(1)
        var1 = var1.split('\n', 1)[1]  
    nums = re.split(f"[{delimiter}\n]", var1)
    result = sum(int(num) for num in nums if num.isdigit() and int(num) <= 1000)
    return result

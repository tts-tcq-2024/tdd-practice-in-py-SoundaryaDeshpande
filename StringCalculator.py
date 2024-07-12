import re

def add(var1): 
    if var1 == "" or var1 == "0":
        return 0
    
    delimiter = ','  # Default delimiter
    
    if var1.startswith("//"):
        delimiter_check = re.match(r"//(.+)\n", var1)
        if delimiter_check:
            delimiter = delimiter_check.group(1)
            var1 = var1.replace(f"//{delimiter}\n", "", 1)
    var2 = re.split(rf"[{delimiter}\n]", var1)
    result = 0
    for num in var2:
        if num.strip().isdigit():
            num_int = int(num.strip())
            if num_int <= 1000:
                result += num_int
    
    return result

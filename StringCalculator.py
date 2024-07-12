import re
def add(var1):
    if var1 == "" or var1 == "0":
        return 0
    delimiter = ','  
    if var1.startswith("//"):
        delimiter = var1[2]  
        var1 = var1[4:]      
    var2 = re.split(rf"{re.escape(delimiter)}|\n", var1)
    var3 = filter(lambda num: num.isdigit() and int(num) <= 1000, var2)
    result = sum(map(int, var3))
    return result

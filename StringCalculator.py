import re
def add(var1): 
    if var1 == "" or var1 == "0":
        return 0
    delimiter = delimiter_call(var1)
    var1=numbers(var1)
    var2=split_numbers(var1,delimiter)
    result=valid_number(var2)
    return result
def delimiter_call(var1):
     if var1.startswith("//"):
         return var1[2]
     else:
         return ','
def numbers(var1):
     if var1.startswith("//"):
         return var1[4:]
     else:
         return var1
def split_numbers(var1,delimiter):
    return re.split(rf"{re.escape(delimiter)}|\n", var1)
def summing_valid_numbers_only(var2):
    return sum(int(num) for num in var2 if valid_number(num))
def valid_number(num_str):
    try:
        num=int(num_str)
        return num<=1000
    except ValueError:
        return false
    
   

    
    
    

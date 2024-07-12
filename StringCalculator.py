def add(var1): #test case 1
  if (var1== "" or var1 == "0"):
    return 0
  elif("var1"):
    var2=var1.split(',')
    num1=int(var2[0].strip())
    num2=int(var2[1].strip())
    if(num1>1000):
      num1=0
    if(num2>1000):
      num2=0
    res=num1+num2
    return res
  else:
    return 
    
     
 
  

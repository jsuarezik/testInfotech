def check(string):
    opens = []
    if len(string) == 0: 
        return False
        
    for i in range(len(string)):
        if string[i] == '(':
            opens.append(string[i])
        else :
            if len(opens) == 0:
                return False
            del(opens[-1])
            
    return len(opens) == 0

#Inserte String a chequear 
print (check(""))
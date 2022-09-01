def regexque(s,p):
    s=list(s)
    for i in s:
        if i=="*":
            s[1]=s[0]
            pass
    if s[0]=="." and s[1]:
        s=p
    if list(s)==list(p):
        return("True")
    else:
        return("False")
s=input("Regex Condition:-")
p=input("Check Condition:-")
z=regexque(s,p)
print(z)




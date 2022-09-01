# Container with most water (leetcode problem). 

x=[1,2,3]
y=[]
for i in range(len(x)):
    for j in range(i+1,len(x)):
        if(x[i]>x[j]):
            area=(j-i)*x[j]
            y.append(area)
            # print(y)
        else:
            area=(j-i)*x[i]
            y.append(area)
print(max(y))


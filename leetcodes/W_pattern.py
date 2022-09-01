# W pattern using python

n = int(input("Enter Number-"))
s = ((n)*(2)-3)
m=s
for i in range(n):
   if i == 0:
      print(f"*{s*' '}*{s*' '}*")
   elif i == (n-1):
      print(f"{(n-1)*' '}*{s*' '}*{(n-1)*' '}")
   else:
      m=m-2
      print(f"{i*' '}*{m*' '}*{((i*2)-1)*' '}*{m*' '}*{i*' '}")
# ZigZag Conversion (leetcode problem). 

def zigzag(s, n):
    G = ""
    E = (n - 1)*2
    d = 0 
    for i in range(n):
        if i < len(s):
            G += s[i]
        j = i
        while j < len(s):
            j += E
            if(E and j < len(s)): 
                G += s[j]
            j += d
            if(d and j <len(s)):
                G += s[j]
        E -= 2
        d += 2
    return G
sol = zigzag('PAYPALISHIRING', 3)
print("Zigzag string-",sol)
          
            
# word1 = input("Enter Word1:-")
# word2 = input("Enter Word2:-")

# def edit_distance(word1, word2)
#   m  = word1.length
#   n= word2.length
#   d = Array.new(m+1) { Array.new(n+1, 0) }
  
#   x=0
#   y=0
#   (m) = |i|
#      y.upto(n) = |j|
#       if i==0 &&  j==0:
#         d[i][j]=0
      
#       elif i==0
#         d[i][j]=d[i][j-1]+1

#       elif j==0
#         d[i][j]=d[i-1][j]+1

#       else:

#         if word1[i-1] == word2[j-1]:          
#           d[i][j]=d[i-1][j-1]
#         else: 
#           d[i][j]=1+[d[i-1][j],d[i][j-1],d[i-1][j-1]].min  
#           return d[m][n]
 
  

# print(edit_distance("horse","ror"))
# print (edit_distance("intention","execution"))
# print (edit_distance("bat","bar"))

lst = [12,3,2,33,32,1,34,5,4]
print(lst)
 #mylen = len(lst)
for i in range (len(lst)-2,-1,-1):
  for j in range (i+1):
   if lst[j] > lst[j+1]:
         temp = lst[j]
         lst[j]=lst[j+1]
         lst[j+1]=temp
print(lst)
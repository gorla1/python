even = []
odd = []
even_Sum = 0
odd_Sum = 0
n=int(input("enter the number of elements"))
for i in range(0,n):
         num=int(input())
         if num % 2 == 0:even.append(num)
         else:odd.append(num)
for x in range(0,len(even)):even_Sum=even_Sum+even[x]
for x in range(0,len(odd)):odd_Sum=odd_Sum+odd[x]
total = even_Sum - odd_Sum
print(even,odd,even_Sum,odd_Sum,total)

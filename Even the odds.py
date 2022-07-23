
def Eventheodds(num): 
flag = 0
l = ['1','3','5','7','9']
for digit in str(num):
    print(digit)
    if not digit in l:
        print('False')
        flag =1 
        break

if flag == 0 :
    print ("True\n")

while True:
num =input(' Enetr your number: ')

#checking the num is negative or not
if not num.isnumeric():
    print('please enter an integer number')
elif int(num)<0:
   print('please enter a posetive number') 
    
else: 
    break      


         
print(Eventheodds(num))
    
      
    

    

    





    
        

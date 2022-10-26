a = 10; b= 20 
def my_function():
    global a 
    a=11; b=21
my_function ()
print(a)
print(b)


x='one'
if x==0:
    print('False')
elif x==1:
    print('True')
else: print('Something else')
#prints 'Something else'

x=0 
while x<3 : print(x); x+=1

a= [1,2,3,4,5,7,7,8,89]
print(a)
a.insert(2 ,80)
print(a)


x = "Amani Meshak0"
print(x)
print(x[len(x)-1])

for i in enumerate(x[0:5]): print(1)

print(x[:5] + 'Best' + x[5:])

#conversion of a string to integer
x = "20"
print(x)

print(type(x))

x = int(x) + 20 
print(type(x))
print(x)

items = [["rice",2.3,8], ["flour",1.9,5],["Corn",4.7,6]]
for item in items :
    print("Product: %s Price: %.2f Quality: %i" %(item[0], item[1], item[2])) 

items[1][1]= items[1][1] * 1.2
print(items[1][1])
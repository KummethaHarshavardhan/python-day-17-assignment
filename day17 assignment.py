
###lambda():

#addition
total= lambda a,b,c:a+b+c
print(total(10,20,30))


#product
product=lambda a,b,c:a*b*c
print(product(76,56,78))


#squre  one value
square=lambda a:a ** 2
print(square(5))
 

#area of circle
area_of_circle=lambda radius:3.14 * radius ** 2
print(area_of_circle(5))


#volume of cube
volume_of_cube=lambda side:side ** 3
print(volume_of_cube(5))


### map():

#square of numbers
numbers = [1,2,3,4,5]
squared_numbers=list(map(lambda x: x ** 2,numbers))
print(squared_numbers)

#volume of cube
sides=[5,10,15,20]
volumes=list(map(lambda side:side**3,sides))
print(volumes)

#area of circle
areas=[5,10,15,20]
circle=list(map(lambda radius:3.14*radius**2,areas))
print(circle)

#add 1 to the numbers
numbers=[1,2,3,4,5]
increment_number=list(map(lambda x:x+1,numbers))
print(increment_number)

#area of rectangules
length=[5,10,30]
width=[5,10,15]
areas=list(map(lambda x,y: x*y,length,width))
print(areas)

###filter():

#odd numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
odd_numbers=list(filter(lambda x: x % 2 !=0,numbers))
print(odd_numbers)

#positive numbers
numbers=[-1, 2, -3, 4, 5]
positive_numbers=list(filter(lambda x : x > 0 ,numbers))
print(positive_numbers)

#even indexed values
numbers=[1,2,3,4,5,6,7,8,9,10]
even_index=list(filter(lambda x:numbers.index(x) % 2 == 0,numbers))
print(even_index)

#number greater than 5
numbers=[2,22,5,45,6,1,3,48,99]
number_greater=list(filter(lambda x: x > 5,numbers))
print(number_greater)

#sting greater than 5
string=["harsha","harika","guna","hari","hema","naveen"]
long_string=list(filter(lambda x: len(x) > 5,string))
print(long_string)

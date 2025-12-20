a = (1,3, 4,4, 5,"shivam", "joy","pune")

b = a.count(4)
print(b)

c = a.index(4)
print(c)

#repeated tuple we can repeat tuple  eg 

my_tuple = (1,2,3)

z = my_tuple * 3
print(z)

# membership : you can check if an item exist in a tuple using "in" keyword

my_tuple = (1,2,3)
print(2 in my_tuple) #output : true
print(4 in my_tuple) #output : false

#to find smallest and largest tuple in a function 

print(min(my_tuple)) #output : 1
print(max(my_tuple)) #output : 3

# unpacking : tuples can be unpacked into individual variables 

tuple = (1,2,3)
a,b,c = tuple 
print(a,b,c)



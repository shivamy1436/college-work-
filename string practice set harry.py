#Q.1 

a = input("enter your name: ")
print(f"good afternoon: , {a}")

#Q.2 

a = "<|shivam|>\n you are selected!\n <|12/12/2025>|"
print(a)

#Q.2 other method 
b ='''dear<|name|>,
ypu are selected 
<|date|>'''

print(b.replace ("<|name|>" , "shivam") .replace ("<|date|>","24sept2005"))

#Q.4 to detect double space 

c = "my name is    shivam "
print(c.find("  "))

#Q.5 replaace double space with single 

d  = "shivam is good   boy"

print(d.replace("  ", " "))




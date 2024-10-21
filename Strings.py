# Strings are basically objects rapped around a quoute ('', " ")

print("Hello World")

print(type(" "))
print(type(' '))

# Variables 
# Take variables to be containers that holds
# information with specific name attached to it on your system

name = "Benjamin"
print(name) 

Den = "the lion is in its Den"
print(Den)

print(len(Den))

print(Den.title())
print(Den.capitalize())
print(Den.upper())

He = "HE IS A BOY"
print(He.lower())

y = He.replace("BOY", "GIRL")
print(y)

Brown = " The color is brown"
print(Brown)
print(Brown.lstrip())
tom = 'Tom'

Can = "Can we be friends with   " 
print(Can + tom)
print(Can.rstrip()+" "+tom)

Greet = "Good day"
k = Greet +" "+ tom
print(k)

fname = 'Helen'
lname = 'Paul'

#Format method
Fullname = '{} {}'.format(lname,fname)
print(Fullname)

# f literal
Username = f'{lname} {fname}'
print(Username)

Name = fname, lname
print(Name)

# Partition
ca = "I have fun coding in python"
b = ca.partition('fun')
print(b)

# Indexing
print(b[0])
print(b[1])
print(b[2])
#rpartition

h = 'I have a good Job and the Job is fun!'
d = h.rpartition('Job')

print(d.index('Job'))
print(h.count('Job'))

# Split method!
user = "B-e-n-n-y"
print(user.split('-')) 

a = 'Hello World'
print(a.split(' '))

# Membership
gy = "I am glad to be here!"
print('am' in gy)

print('his' in gy)

# Loop through a string!!
for item in gy:
    print(item)
    
print(fname.split(''))
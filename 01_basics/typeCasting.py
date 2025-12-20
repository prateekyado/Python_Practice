#The process for cinverting one data type to another.

name="Ansrk"
age=21
cgpa=8.74

print(type(name))
#<class 'str'>
cgpa=int(cgpa)
print(cgpa)
#8
print(float(age))
#21.0
name=bool(name) 
print(name)
#true
from converters14 import convert
from parser14 import parse

feet_inches = input("Enter feet and inches: ")

#feet_inches_tuple = parse(feet_inches)
f, i = parse(feet_inches)
print(f,i)
#result = convert(feet_inches_tuple[0], feet_inches_tuple[1])
result = convert(f, i)

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")


feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

#feet_inches_tuple = parse(feet_inches)
f, i = parse(feet_inches)
print(f,i)
#result = convert(feet_inches_tuple[0], feet_inches_tuple[1])
result = convert(f,i)

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")


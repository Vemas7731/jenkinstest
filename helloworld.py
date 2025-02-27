print("Goodbye, World!")

def convert_seconds(seconds) :
    hour = seconds // 3600
    minutes = (seconds - hour * 3600) // 60
    seconds_remaining = seconds - hour * 3600 - minutes * 60
    return hour, minutes, seconds_remaining

hour, minutes, seconds = convert_seconds(5000)
print(hour, minutes, seconds)

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(int(area))

circle_area(7)
circle_area(18)

def greater_value(x, y):
    if x > y:
        return x
    else:
       return y


print(greater_value(10,3*5))

x = 0
while x < 5 :
    print ("haha")
    x += 1

def circle(r):
    area = 3.14 * r**2
    return area

for r in range(0, 71, 14):
    print (r, circle(r))


for n in range(0, 15, 2):
    print(n)
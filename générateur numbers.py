import random

#generate 8 digits random number
def generate_number():
    number = random.randint(10000000, 99999999)
    return number

def write_number(number):
    file = open("numbers.txt",'a')
    file.write(str(number) + "\n")
    file.close()

#repeat 100x
for i in range(100):
    write_number("06" + str(generate_number()))
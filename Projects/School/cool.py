import random
import math
i = 0
while True:
    i += 1
    oldernumber1 = random.uniform(0, 10)
    oldernumber2 = random.uniform(0, 10)
    oldernumber3 = math.sqrt((oldernumber1 ** 2) + (oldernumber2 ** 2))


    oldnumber2 = random.uniform(0, oldernumber3)
    oldnumber1 = math.sqrt((oldernumber3 ** 2) - (oldnumber2 ** 2))
    oldnumber3 = math.sqrt((oldnumber1 ** 2) + (oldnumber2 ** 2))

    if math.isclose(oldernumber3, oldnumber3):
        print("hi")
    else:
        break

    number1 = random.uniform(0, oldnumber3)
    number2 = math.sqrt((oldnumber3 ** 2) - (number1 ** 2))
    number3 = math.sqrt((number1 ** 2) + (number2 ** 2))

    if math.isclose(oldnumber3, number3):
        print("bye")
    else:
        break
    if i == 10:
        break
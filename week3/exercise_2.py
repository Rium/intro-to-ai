from random import randint

def troubleshoot():
    car = [0, 0, 0, 0, 0, 0]

    if working() < 90: car[0] = 1

    if car[0] == 1:
        if working() < 90: car[1] = 1
        if working() < 95: car[2] = 1

    if working() < 95: car[3] = 1

    if car[0] == 1 and car[3] == 1:
        if working() < 99: car[4] = 1

    if car[4] == 1:
        if working() < 99: car[5] = 1

    return tuple(car)

def working():
    return randint(1, 100)

if __name__ == "__main__":
    test_cases = []

    for i in range(100000):
        test_cases.append(troubleshoot())

    # P(B | R,G,¬S)
    approx = []
    counter = 0
    for i in test_cases:
        if i[1] == 1 and i[3] == 1 and i[4] == 0:
            approx.append(i)

    for i in approx:
        if i[0] == 1:
            counter += 1

    print(counter / len(approx))
    # Gives 1, makes sense. If R is 1 B has to be 1

    # P(S | R,I,G)
    approx = []
    counter = 0
    for i in test_cases:
        if i[1] == 1 and i[2] == 1 and i[3] == 1:
            approx.append(i)

    for i in approx:
        if i[4] == 1:
            counter += 1

    print(counter / len(approx))

    # P(S | ¬R,I,G) 
    approx = []
    counter = 0
    for i in test_cases:
        if i[1] == 0 and i[2] == 1 and i[3] == 1:
            approx.append(i)

    for i in approx:
        if i[4] == 1:
            counter += 1

    print(counter / len(approx))
    # These both give ~98% to 99%, which again makes sense.
    # R does not affect S, and both I and G have to be 1 for S to be 1.
    # Thus the only thing that changes is the 99% chance on S.


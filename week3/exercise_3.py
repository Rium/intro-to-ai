from random import randint

def alarm():
    problem = [0, 0, 0]

    if randint(1, 111) == 1: problem[0] = 1
    if randint(1, 365) == 1: problem[1] = 1

    if problem[0] == 1 and problem[1] == 0 and randint(1, 100) < 81: problem[2] = 1
    elif problem[0] == 0 and problem[1] == 1 and randint(1, 100) < 92: problem[2] = 1
    elif problem[0] == 1 and problem[1] == 1 and randint(1, 100) < 97: problem[2] = 1
    elif problem[0] == 0 and problem[1] == 0 and randint(1, 10000) < 95: problem[2] = 1

    return tuple(problem)

if __name__ == "__main__":
    test_cases = []

    for i in range(100000):
        test_cases.append(alarm())

    # 1. Among the tuples with A=1, what is the fraction where B=1?
    approx = []
    counter = 0
    for i in test_cases:
        if i[2] == 1:
            approx.append(i)

    for i in approx:
        if i[1] == 1:
            counter += 1

    print(counter / len(approx))
    # About ~0.13, +-0.01

    # 2. Among the tuples with A=1 and E=1, what is the fraction where B=1?
    approx = []
    counter = 0
    for i in test_cases:
        if i[2] == 1 and i[0] == 1:
            approx.append(i)

    for i in approx:
        if i[1] == 1:
            counter += 1

    print(counter / len(approx))
    # About 0.003. Gave a 0.0 once while I was testing.

    # 3. The first is the chance that when your alarm goes off that you're being burglarised. 
    # The second is that the burgular chose an earthquake as the perfect cover

    # 4. Yeah. The alarm going off due to an earthquake is roughly 3 times higher than someone breaking in.
    # Add to that that most days nothing happens but there's still a chance for the alarm to go off, 13% sounds about right.
    # The tiny chance being both an earthquake and a burglar makes sense too. 
    # Both happening at once is super rare, and there's a chance that the alarm might not even go off

    # 5. Added some notes under the code snippets. 
    # Lowering the n to 10,000 had the values vary more vildly.
    # Increasing it to 1,000,000 made the code slower, and gave roughly the same answers
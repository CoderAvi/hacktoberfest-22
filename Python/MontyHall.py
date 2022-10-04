from random import randint


def simulationstay(n):
    win = 0
    lose = 0
    for i in range(n):
        Car = [randint(1, 3)]
        ChooseP = [randint(1, 3)]
        if Car == ChooseP:
            win += 1
        else:
            lose += 1
    return (win / n)


def simulationchange(n):
    win = 0
    lose = 0
    for i in range(n):
        Car = [randint(1, 3)]
        ChooseP = [randint(1, 3)]
        if Car == ChooseP:
            lose += 1
        else:
            win += 1
    return (win / n)


def maybechange(n):
    win = 0
    lose = 0
    lst = []
    for i in range(n):
        m = randint(1, 4)
        lst.append(m)
    for j in range(n):
        if lst[j] % 2 == 0:
            Car = [randint(1, 3)]
            ChooseP = [randint(1, 3)]
            if Car == ChooseP:
                win += 1
            else:
                lose += 1

        else:
            Car = [randint(1, 3)]
            ChooseP = [randint(1, 3)]
            if Car == ChooseP:
                lose += 1
            else:
                win += 1
    return (win / n)


print("{:20}{:20}".format("I changed my mind:", simulationstay(1000)))
print(
    "{:20}{:15}".format(
        "I did not change my decision:",
        simulationchange(1000)))
print(
    "{:20}{:10}".format(
        "50% of that, I changed my mind:",
        maybechange(1000)))

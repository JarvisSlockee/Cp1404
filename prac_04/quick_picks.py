import random

MIN = 1
MAX = 45
NUM_PER_LINE = 6


def main():
    num_of_quick_picks = int(input("How many quick picks?"))
    while num_of_quick_picks < 0:
        print("Invalid! Please picker a number greater than 0")
        num_of_quick_picks = int(input("How many quick picks?"))

    for i in range(num_of_quick_picks):
        quick_pick = []
        for x in range(NUM_PER_LINE):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("[{:2}".format(number) for number in quick_pick))


main()

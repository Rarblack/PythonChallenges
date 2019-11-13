import random

def get_random_10_numbers():
    lottery_numbers = range(1, 51)
    selected_numbers = []

    times = 10
    while(times != 0):
        random_int = random.randint(1, 51)
        if(random_int in selected_numbers):
            continue
        selected_numbers.append(random_int)
        times -= 1

    return selected_numbers

if __name__ == "__main__":
    print(get_random_10_numbers())
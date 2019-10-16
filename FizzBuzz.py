def div_by(num, divisor):
    return (num % divisor) == 0


def print_num(num):
    if div_by(num, 3) and div_by(num, 5):
        print('fizzbuzz')

    elif div_by(num, 3):
        print('fizz')

    elif div_by(num, 5):
        print('buzz')

    else:
        print(num)


for x in range(0, 21):
    print_num(x)

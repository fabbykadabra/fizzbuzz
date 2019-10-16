def div_by(num, divisor):
    return (num % divisor) == 0


def test_div_by():
    assert div_by(4, 3) == False
    assert div_by(3, 3) == True


def return_fizz_buzz_or_num(num):
    if div_by(num, 3) and div_by(num, 5):
        return 'FizzBuzz'
    elif div_by(num, 3):
        return 'Fizz'
    elif div_by(num, 5):
        return 'Buzz'
    else:
        return num


def run_fizz_buzz():
    for x in range(0, 21):
        print( return_fizz_buzz_or_num(x) )



def test_return_fizz_buzz_or_num():
    assert return_fizz_buzz_or_num(3) == 'Fizz'
    assert return_fizz_buzz_or_num(4) == 4
    assert return_fizz_buzz_or_num(5) == 'Buzz'
    assert return_fizz_buzz_or_num(15) == 'FizzBuzz'


run_fizz_buzz()

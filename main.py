def reversed_int(string):
    """Convert string to int"""
    string = string.strip('][').replace(', ', '').replace(',', '')
    reversed_string = ''.join(list(reversed(string)))
    return int(reversed_string)


def calculate_numbers(first_number, second_number):
    """Calculate two numbers"""
    return reversed_int(first_number) + reversed_int(second_number)


def reversed_list(amount):
    """Convert total sum to list"""
    return list(map(int, str(amount)))[::-1]


def user_process():
    """User enters data"""
    first_list = input('Enter first list: ')
    second_list = input('Enter second list: ')
    total_sum = calculate_numbers(first_list, second_list)
    result = reversed_list(total_sum)
    print(result)
    return result


while True:
    try:
        user_process()
        exit_answer = input('Do you want to continue? y/n \n')
        if exit_answer == 'n':
            print('Bye!!!')
            break
    except Exception as e:
        print('Error, Try again')

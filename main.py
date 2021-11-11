def reversed_int(string):
    string = string.strip('][').replace(', ', '').replace(',', '')
    reversed_string = ''.join(list(reversed(string)))
    return int(reversed_string)


def calculate_numbers(first_number, second_number):
    return reversed_int(first_number) + reversed_int(second_number)


def reversed_list(amount):
    return list(map(int, str(amount)))[::-1]


while True:
    first_list = input('Enter first list: ')
    second_list = input('Enter second list: ')
    total_sum = calculate_numbers(first_list, second_list)
    result = reversed_list(total_sum)
    print(result)

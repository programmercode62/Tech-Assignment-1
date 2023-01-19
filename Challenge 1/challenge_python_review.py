import math


def print_squares():
    """
    Docstring
    """
    # code
    for i in range(1, 11):
        print(i*i)


def average(num_list):
    """
    First we checked if the type of the input is not a list: should return None
    Then we checked if it is an empty list: should return 0
    Lastly, we checked each element if any of them is string: return None
    """
    # checking if input is a list
    if type(num_list) != list:
        return None

    # checking if length of input is 0
    if len(num_list) == 0:
        return 0

    # checking if every element is valid
    for element in num_list:

        # if current element is string: return None
        if type(element) == str:
            return None

    # calculating the average
    avg = sum(num_list) / len(num_list)

    return avg


def is_prime(number):
    """
    First we checked the number is less than 2 : return False
    Then we divide the number with all numbers from 2 and immediate before the number.
    If in any case, remainder is 0, return False
    """

    # checking if the number is < 2
    if number < 2:
        return False

    # divide the number from 2 to immediate before that number
    for i in range(2, number):

        # checking if the remainder is zero
        if number % i == 0:
            return False

    return True


def prime_100():
    """
    First 100 prime numbers using while loop. 
    Count variable will count the number of primes
    start is the starting number and increment by 1 each time
    result list will have all the prime numbers
    """

    # variables
    count = 0
    start = 0
    result = []

    # checking count in while loop
    while count < 100:

        # checking if the number is prime
        if is_prime(start) == True:

            # adding it to the result list
            result.append(start)
            # update the count variable
            count += 1

        # moving to the next number
        start += 1

    return result


def count_letters(string):
    """
    make the string lowercase
    convert it to a list of elements
    check each element is letter or not
    if letter, assign it to the dictionary
    """

    # make the string lower case
    string = string.lower()

    # convert to list of elements
    letter_list = list(string)

    result = {}

    # looping through each element in the string
    for element in letter_list:

        # checking if the element is a lowercase letter
        if ord(element) >= 97 and ord(element) <= 122:

            # if letter already in the dictionary as a key
            if element in result.keys():

                # increment the previous value of the key in the dictionary
                result[element] += 1

            # letter not present in the dictionary as a key
            else:
                # create letter key in the dictionary and assign value 1
                result[element] = 1

    # result.items() get all the items in a list of tuples
    # "sorted" will sort the list in ascending order
    # dict will convert it back to a dictionary
    sorted_result = dict(sorted(result.items()))

    return sorted_result


def filter_strings(string_list):
    """
    check each string in the list following:
    1. if the string has at least 5 letters
    2. if it contains at least one vowel
    """

    result = []

    # looping through each string
    for string in string_list:

        # at first checking the string has at least 5 letters
        if len(string) >= 5:

            # make the string a list of letters
            letter_list = list(string)

            # looping through each letter
            for letter in letter_list:

                # checking if the letter is vowel
                if letter in ['a', 'e', 'i', 'o', 'u']:

                    # adding the string to the result list
                    result.append(string)

                    # break to stop the current for loop, so we can move to the next string
                    break

    return result


def is_palindrome(number):
    """
    Steps:
    Convert the number to a string. It will be easier to generate the flipped version
    flip the string
    compare original and flipped version
    """
    # convert number to string
    string_number = str(number)

    # flip the string using reversed method.
    # Used join with empty delemeter to convert it back to a string
    reversed_number = "".join(reversed(string_number))

    # check if flipped version matched with original version
    if string_number == reversed_number:
        return True

    # doesn't match
    else:
        return False


# Any loose bits of code should be moved into this block print('Test Case 1')
if __name__ == '__main__':
    print_squares()
    print(average([3, 4, 5, 6]))
    print(average([-2.3, 45, 0.111, 11/6]))
    print(average([]))  # return 0
    print(average([1.0, 1.0, -math.inf]))
    print(average([1, 3.14, "h"]))
    print(average("hello?"))
    print(average([1, 2, 3, 4].extend([5])))  # what happens here?
    print(prime_100())
    print(count_letters("The quick brown fox jumps over the lazy dog."))
    print(count_letters("Web serving with FastAPI!"))
    print(filter_strings(["The", "Brown", "rrrrrrr", "Serving"]))
    print(filter_strings(["ertty", "tljklkj", "asdf", "iytioo"]))
    print(filter_strings(["jhgkkj", "qwqert", "trrurii", "dfgjkl"]))
    print(filter_strings(["The", "sfdfffh", "rrrrrrr", "Serving"]))
    print(is_palindrome(1234567.7654321))
    print(is_palindrome(-0.123))

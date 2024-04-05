my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

def odd_or_even(number):
    return 'even' if number % 2 == 0 else 'odd'

# new_list = ['even' if num % 2 == 0 else 'odd' for num in my_list]
new_list = [odd_or_even(num) for num in my_list]

print(new_list)
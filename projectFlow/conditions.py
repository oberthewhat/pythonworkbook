age = int(input("How old are you? "))

if 16 <= age <= 65:
    print('have a good day at work')
else:
    print('enjoy your free time')

print("-" * 50)

if age < 16 or age > 65:
    print('enjoy  your free time')
else:
    ('Have a good day at work')
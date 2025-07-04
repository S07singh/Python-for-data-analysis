# Logical operators = evaluate multiple conditions (or, and, not)
#                       or - at least one condition must be true
#                       and = both condition must be true
#                       not = inverts the condition (not False, not True)


temp = 23
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

tempe = 34
is_sunny = True

if tempe >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif tempe <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 28 > tempe > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif tempe >= 28 and not is_sunny:
    print("It is HOT outside")
    print("It is CLOUDY")
elif tempe <= 0 and not is_sunny:
    print("It is COLD outside")
    print("It is CLOUDY")
elif 28 > tempe > 0 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY")



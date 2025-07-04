'''
| Method                    | Description                           | Example                                   |
| ------------------------- | ------------------------------------- | ----------------------------------------- |
| `lower()`                 | Converts to lowercase                 | `'Hello'.lower()` → `'hello'`             |
| `upper()`                 | Converts to uppercase                 | `'hello'.upper()` → `'HELLO'`             |
| `capitalize()`            | Capitalizes first letter              | `'python'.capitalize()` → `'Python'`      |
| `title()`                 | Capitalizes first letter of each word | `'hello world'.title()` → `'Hello World'` |
| `strip()`                 | Removes leading/trailing spaces       | `'  hi  '.strip()` → `'hi'`               |
| `lstrip()` / `rstrip()`   | Removes spaces from left/right        | `'  hi'.lstrip()` → `'hi'`                |
| `replace(old, new)`       | Replaces substring                    | `'cat'.replace('c', 'b')` → `'bat'`       |
| `find(sub)`               | Returns index of first occurrence     | `'hello'.find('l')` → `2`                 |
| `count(sub)`              | Counts occurrences                    | `'banana'.count('a')` → `3`               |
| `startswith(sub)`         | Checks if starts with substring       | `'apple'.startswith('a')` → `True`        |
| `endswith(sub)`           | Checks if ends with substring         | `'apple'.endswith('e')` → `True`          |
| `split(sep)`              | Splits string into list               | `'a,b,c'.split(',')` → `['a', 'b', 'c']`  |
| `join(list)`              | Joins list into string                | `'-'.join(['a', 'b'])` → `'a-b'`          |
| `isalpha()`               | Checks if all letters                 | `'abc'.isalpha()` → `True`                |
| `isdigit()`               | Checks if all digits                  | `'123'.isdigit()` → `True`                |
| `isalnum()`               | Checks if letters and digits          | `'abc123'.isalnum()` → `True`             |
| `islower()` / `isupper()` | Checks if all lowercase/uppercase     | `'abc'.islower()` → `True`                |
| `swapcase()`              | Swaps case                            | `'HeLLo'.swapcase()` → `'hEllO'`          |

'''

# print(help(str))

name = input("Enter the your name: ")
phone_number = input("Enter your phone number: ")

# result = name.find("u")
# result = name.rfind("s")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = name.isalpha()
# result = phone_number.count("-")
phone_number = phone_number.replace("-", "")

print(phone_number)

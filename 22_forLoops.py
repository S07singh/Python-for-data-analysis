# for loops = execute a block of code a fixed number of times.
#             you can iterate over a range, string, sequence, etc.

# we can use range(start, end, step) or reversed(range(start, end, step))
# for x in reversed(range(1, 11, 2)):
#     print(x)
# print("HAPPY NEW YEAR")

# credit_card = "1234-5678-9012-3456"
#
# for i in credit_card:
#     print(i)

for i in range(1, 21):
    if i == 13:
        break # continue
    else:
        print(i)
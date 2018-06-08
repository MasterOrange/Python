#!/usr/local/bin/python3.5

# Defining floats
myfloat = float(7)
print(myfloat)

# Single and double quotes are the same, just use single

string1 = "My string's here."
string2 = 'My string\'s here.'
print(string1 + '\n' + string2)

# isinstantce() tests the class of the object/variable

# A test to see if the object is a float
myFloat = float(3)
if isinstance(myFloat, float):
    print("myFloat is a float: %f" % myFloat)
else:
    print("it's not a float")

# Printing % sign
string3 = 'of a string variable'
print("Is a substitution...%s or a %% (percent) sign" % string3)

# Formatting operators:
# %s -> string (or any object with string representation, like numbers)
# %d -> integers
# %f -> floats
# %.(number of digits)f -> float with fixed no. of digits to the right of decimal
# %x/%X -> integers in hex representation (lowercase/uppercase)

# Reversing a string
print(string1[::-1])

# string.startswith() | string.endswith() tests the contents of string
# returns TRUE or FALSE
# string.split('delimiter') e.g string1.split(' ') uses spaces as delim.

# == matches the values of the variables
# 'is' matches the instances themselves

numbers = [ 951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527 ]

for num in numbers:
    if num == 237:
        break
    
    if num % 2 == 1:
        continue

    print(num)

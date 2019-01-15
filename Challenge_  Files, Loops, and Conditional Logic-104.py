## 3. Read the File Into a String ##

f = open("dq_unisex_names.csv", "r")
names = f.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []
for name in names_list:
    comma_list = name.split(",")
    nested_list.append(comma_list)
print(nested_list[0:5])

## 6. Convert Numerical Values ##

print(nested_list[0:5])
combined_list = []
numerical_list = []
for line in nested_list:
    variable_list = line[0]
    float_list = float(line[1])
    combined_list = [variable_list, float_list]
    numerical_list.append(combined_list)
print(numerical_list[0:5])

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for value in numerical_list:
    if int(value[1] >= 1000):
        thousand_or_greater.append(value[0])
print(thousand_or_greater[0:10])
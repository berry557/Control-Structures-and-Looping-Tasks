# Task 1: Conditional If-Else Statement
number = 5
if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# Task 2: Adding Elif to Check if Number is Zero
number = 0
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Task 3: Print Characters of a String Individually
course_name = "UCIL22212"
for char in course_name:
    print(char)

# Task 4: Print Elements in Lowercase or Uppercase
days = ["mOnDay", "TueSDAY", "Wednesday", "thursday", "FridaY"]

for day in days:
    print(day.lower())

for day in days:
    print(day.upper())

# Task 5: Print Only Integer Elements from a List
element_list = ["Car", "Museum", 15, "Knight", 20, 30]
for element in element_list:
    if type(element) == int:
        print(element)

# Task 6: Print Only String Elements from a List
for element in element_list:
    if type(element) == str:
        print(element)

# Task 7: Print All Even Numbers Between 1 and 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Task 8: Iterate Over List Until Element 20 is Found
element_list = ["Car", "Museum", 15, "Knight", 20, 30]
index = 0

while index < len(element_list):
    print(element_list[index])
    
    if element_list[index] == 20:
        print("Element 20 Found")
        break
    index = index + 1

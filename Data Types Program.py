# We Are Going To Make A Dictionary First!
a = {}
n = int(input("Number Of Students You want in the list: "))
for i in range(n):
    name = input("Enter The Name Of The Student: ")
    rollno = int(input(f"Enter The Roll No of {name}: "))
    a[name] = rollno
print("Printing The Names Of The Students in The Data: ", a)

# Now that We Have Created The Dictionary We Will Find Out How Many Students are there and their name

keys1 = a.keys()
print("Number Of Students In The Data: ", len(keys1))  # Print the number of students directly

values1 = a.keys()
print("Names Of The Students In the Data: ", list(values1))  # Convert values to list and print directly

# We Are going to ask the user if they want to find a certain student if they exist in the data
ask1 = input("Want to Find if A Student exists In The dataset (Y/N): ").upper()

if ask1 == "Y":
    name_of_stu = input("Enter The Name of The Student You want To find in the data: ")
    if name_of_stu in a:
         print("Yes, the Student Exists In the Database!")
    else:
        print("No, The Student Does Not exist In the Database!")
else:
    print("We Won't Find The Student Data!")



     






# List of 20 students
# Each student is represented as a tuple: (First_Name, Surname)
students = [
("Vishnu", "madana"),
("Vishnu", "Munagala"),
("Srinu",  "sharma"),
("padma", "Chowdary"),
("rajesh", "yerra"),
("Venkat" , "rojulu"),
("Srikanth", "velaga"),
("Venkatesh", "velaga"),
("ramu", "gali"),
("rakesh", "modugula"),
("swetha", "rani"),
("Vivek", "sharma"),
("raju", "podusu"),
("Lakshmi", "kasu"),
("sai",  "madusa"),
("yugandhar", "Munagala"),
("raju", "ginna"),
("srikar", "valluri"),
("Kusuma", "rajula"),
("Sanjay" , "medisetti")
]

# Dictionary to store the first occurrence of each student name
# Key   -> First Name
# Value -> Surname
unique_students = {}

# List to store students who have the same first name
# but different surname (only one duplicate is kept)
duplicates = []

# Loop through each student in the list
for first_name, surname in students:

    # If the first name is not already present,
    # store it in the dictionary
    if first_name not in unique_students:
        unique_students[first_name] = surname

    # If the first name already exists
    else:
        # Check if the surname is different
        if unique_students[first_name] != surname:
            # Add this student as a duplicate
            duplicates.append((first_name, surname))

# Print the result
print("Students with same first name but different surname:")

# Loop through the duplicates list and display each student
for name in duplicates:
    print(name)

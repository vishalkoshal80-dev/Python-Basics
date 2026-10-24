name = input("Enter Student Name: ")
math = float(input("Enter your Math's Marks(out of 100):"))
science = float(input("Enter your Science's Marks(out of 100):"))
social_science = float(input("Enter your social_science's Marks(out of 100):"))
hindi = float(input("Enter your hindi's Marks(out of 100):"))
computer = float(input("Enter your computer Marks(out of 100):"))

total = math + science + social_science + hindi + computer
percentage = (total/500)*100

print("\n------Student  Result-------")
print("Student Name:", name)
print("Total Marks: ", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade : A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: F")
print("----------------------------------------")

for i in range (5):
    mark = int(input(f"Enter your mark {i+1}: "))

    if mark<0 or mark>100:
        print("Invalid input.")
        break

    if mark>=75:
        grade = "A"

    elif mark>=65:
        grade = "B"

    elif mark>=55:
        grade = "C"

    elif mark>=45:
        grade = "S"

    else:
        grade = "F"
    

    print ("Grade : ", grade)

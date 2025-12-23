print("Decision Tree: Student Pass / Fail Prediction")

hours = int(input("Enter number of study hours: "))
attendance = int(input("Enter attendance percentage: "))

if hours >= 6:
    if attendance >= 75:
        print("Result: PASS")
    else:
        print("Result: FAIL")
else:
    print("Result: FAIL")

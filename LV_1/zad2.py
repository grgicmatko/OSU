
try:
    grade = float(input("Unesi ocjenu [0.0,1.0]: "))
    if grade < 0.0 or grade > 1.0:
        print("Grade is out of range")
    elif grade < 0.6:
        print("F")
    elif grade < 0.7:
        print("D")
    elif grade < 0.8:
        print("C")
    elif grade < 0.9:
        print("B")
    else:
        print("A")
except:
    print("Not a number")
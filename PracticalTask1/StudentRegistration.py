# print headings
def printHeadings():
    print("\n---HOLMESGLEN INSTITUTE---")
    print("\n{0:<8} {1:<18} {2:<20} {3:>12}".format("ID", "NAME", "COURSE", "FEE"))
printHeadings()

# create local variable totalFees
totalFees = 0.00


# create empty list for storing student details
studentDetails = []


# input student details
def inputStudentDetails():
    global totalFees

    studentID = input("Input student ID:")
    studentName = input("Input student name:")
    course = input("Input course name:")
    courseFee = float(input("Input course fee:"))
    dollarCourseFee = "${:,.2f}".format(courseFee)
    totalFees += courseFee

    studentDetails.append("{0:<8} {1:<18} {2:<20} {3:>12}".format(studentID, studentName, course, dollarCourseFee))

    printHeadings()
    print("{0:<8} {1:<18} {2:<20} {3:>12}".format(studentID, studentName, course, dollarCourseFee))
    return totalFees


# output total fee
def outputTotalFee():
    print("\nTotal fee:  ", "{:,.2f}".format(totalFees))


# input the details for three students and display on screen with total fee
inputStudentDetails()
inputStudentDetails()
inputStudentDetails()
print()
printHeadings()
print(studentDetails[0])
print(studentDetails[1])
print(studentDetails[2])
outputTotalFee()
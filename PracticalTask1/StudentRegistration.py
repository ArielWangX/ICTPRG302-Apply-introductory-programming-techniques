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

    # import simpledialog object
    from tkinter import simpledialog
    # get user input
    studentID = simpledialog.askstring('Dialog Title', 'Input student ID:')
    studentName = simpledialog.askstring('Dialog Title', 'Input student name:')
    course = simpledialog.askstring('Dialog Title', 'Input course name:')
    courseFee = simpledialog.askfloat('Dialog Title', 'Input course fee:')

    # if: any information in user input is null or empty
    # tell user input student details unsuccessful
    # else: format the user input and gather student course fee into total fee
    if (studentID is None or not studentID) or (studentName is None or not studentName) or (course is None or not course) or (courseFee is None):
        print("\nInput student details unsuccessful\n")
    else:
        # add dollar sign of the course fee
        dollarCourseFee = "${:,.2f}".format(courseFee)

        # gather student course fee into total fee
        totalFees += courseFee

        # format student information
        studentDetails.append("{0:<8} {1:<18} {2:<20} {3:>12}".format(studentID, studentName, course, dollarCourseFee))

        # output formated heading and student information
        printHeadings()
        print("{0:<8} {1:<18} {2:<20} {3:>12}".format(studentID, studentName, course, dollarCourseFee))

    # return total fee
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
# print out student details in studentDetails list
for studentDetail in studentDetails:
    print(studentDetail)
outputTotalFee()
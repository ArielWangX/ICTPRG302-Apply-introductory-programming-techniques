# # opening file Employees.txt in read mode
rawEmployeeFile = open("E:\\Programming\\ICTPRG302 Apply introductory programming\\AT1\\Employees.txt", "r")

# reading the file
data = rawEmployeeFile.readlines()

# remove "\n" in each elment in data list
for i in range(0, len(data)):
    if data[i].endswith("\n"):
        data[i] = data[i][:-1]

# create list to store employee txt information
employeeList = []


# analyze data - store every employee information in a dictionary and add this dictionary to employeeList
def analyzeEmployeeTxtData(dataList):  
    id = ""
    name = ""
    position = ""
    salary = 0.00
   
    i = 0
    while i < len(dataList):
        id = dataList[i]
        name = dataList[i+1]
        position = dataList[i+2]
        salary = dataList[i+3]

        # store each employee information in a dictionary
        employee = {
            "ID": id,
            "Name": name, 
            "Position": position,
            "Salary": salary
        }
        
        # add employee dictionary into employee list
        employeeList.append(employee)    
        i += 4

        
#  call analyze data function to make a list of dictionary to store employee information    
analyzeEmployeeTxtData(data)


# display each record of data on the screen
def displayEmployeeTxtData(employeeList):
    # get value from employee dictionary
    for employee in employeeList:
        id = employee["ID"]
        name = employee["Name"]
        position = employee["Position"]
        salary = float(employee["Salary"])

        # add dollar sign to salary
        dollarSalary = "${:,.2f}".format(salary)
        
        # print each employee information
        print(id + " " + name + " " + position + " " + dollarSalary + "\n")


# call the function to display each record to the screen    
displayEmployeeTxtData(employeeList)


# total pay of all employees
def totalPay(employeeList):
    # create total pay variable
    totalPay = 0.00

    for employee in employeeList:
        salary = float(employee["Salary"])

        totalPay += salary
        
    return round(totalPay, 2)


# number of records
def numOfRecords(employeeList):
    # create records variable
    records = 0

    records = len(employeeList)
    return records


# average pay
def averagePay(employeeList):
    # create average pay variable
    averagePay = 0.00

    averagePay = totalPay(employeeList) / numOfRecords(employeeList)

    # round average pay to 2 decimal places and return
    return round(averagePay, 2)


# total pay for Managers
def managersTotalPay(employeeList):
    # create total pay variable
    managersTotalPay = 0.00

    for employee in employeeList:
        if employee["Position"] == "Manager" :
            managersTotalPay += float(employee["Salary"])
        else:
            continue
    
    return round(managersTotalPay, 2)
    

# total pay for Sales
def salesTotalPay(employeeList):
    # create total pay variable
    salesTotalPay = 0.00

    for employee in employeeList:
        if employee["Position"] == "Sales" :
            salesTotalPay += float(employee["Salary"])
        else:
            continue
    
    return round(salesTotalPay, 2)


# total pay for Administration
def adminTotalPay(employeeList):
    # create total pay variable
    adminTotalPay = 0.00

    for employee in employeeList:
        if employee["Position"] == "Administration" :
            adminTotalPay += float(employee["Salary"])
        else:
            continue
    
    return float(f"{adminTotalPay:.2f}")


# display on screen:
# the total pay of all employees
# the number of records processed
# the average pay
# the total pay for the three types of employee positions (Managers, Sales or Administration)
def payrollReport(employeeList):
    print("Total payroll:" + " " + "${:,.2f}".format(totalPay(employeeList)))
    print("Number on payroll:" + " " + str(numOfRecords(employeeList)))
    print("Average pay:" + " " + "${:,.2f}".format(averagePay(employeeList)))
    print("")
    print("Total pay for:")
    print("Managers " + "${:,.2f}".format(managersTotalPay(employeeList)))
    print("Sales " + "${:,.2f}".format(salesTotalPay(employeeList)))
    print("Admin " + "${:,.2f}".format(adminTotalPay(employeeList)))


# call payrollReport function and display payroll report on screen    
payrollReport(employeeList)


# save payroll report to text file
def exportPayrollReport(employeeList):
    # will create a file, return an error if the file exist
    payrollReport = open("E:\Programming\ICTPRG302 Apply introductory programming\AT1\PayrollReport.txt", "w")

    # export payroll report into file
    payrollReport.write("Total payroll:" + " " + "${:,.2f}".format(totalPay(employeeList)))
    payrollReport.write("\nNumber on payroll:" + " " + str(numOfRecords(employeeList)))
    payrollReport.write("\nAverage pay:" + " " + "${:,.2f}".format(averagePay(employeeList)))
    payrollReport.write("\n")
    payrollReport.write("\nTotal pay for:")
    payrollReport.write("\nManagers " + "${:,.2f}".format(managersTotalPay(employeeList)))
    payrollReport.write("\nSales " + "${:,.2f}".format(salesTotalPay(employeeList)))
    payrollReport.write("\nAdmin " + "${:,.2f}".format(adminTotalPay(employeeList)))

    payrollReport.close()


# call exportPayrollReport function and export payroll report to text file    
exportPayrollReport(employeeList)

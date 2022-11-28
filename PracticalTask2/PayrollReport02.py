# create list to store employee csv information
employeeList = []

# import csv module
import csv

# open and read file employees.csv into a dictionary
# store every dictionary into list
with open("E:\\Programming\\ICTPRG302 Apply introductory programming\\AT1\\employees.csv", "r") as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        employeeList.append(dict(row))


# display each record of data on the screen
def displayEmployeeCsvData(employeeList):
    # get value from employee dictionary
    for employee in employeeList:
        id = employee["锘縀mpId"]   # the title from original csv file
        name = employee["Name"]
        position = employee["Position"]
        salary = float(employee["Salary"])

        # add dollar sign to salary
        dollarSalary = "${:,.2f}".format(salary)
        
        # print each employee information
        print(id + " " + name + " " + position + " " + dollarSalary + "\n")


# call the function to display each record to the screen    
displayEmployeeCsvData(employeeList)


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


# save payroll report to csv file
def exportPayrollReport(employeeList):
    # will create a file and open to write
    payrollReport = open("E:\Programming\ICTPRG302 Apply introductory programming\AT1\PayrollReport.csv", "w")

    # prepare data for csv file
    totalPayment = totalPay(employeeList)
    num = numOfRecords(employeeList)
    averagePayment = averagePay(employeeList)
    managersTotalPayment = managersTotalPay(employeeList)
    salesTotalPayment = salesTotalPay(employeeList)
    adminTotalPayment = adminTotalPay(employeeList)

    # export payroll report into file
    payrollReport.write(f"Total payroll, {totalPayment}")
    payrollReport.write(f"\nNumber on payroll, {num}")
    payrollReport.write(f"\nAverage pay, {averagePayment}")
    payrollReport.write("\n")
    payrollReport.write("\nTotal pay for")
    payrollReport.write(f"\nManagers, {managersTotalPayment}")
    payrollReport.write(f"\nSales, {salesTotalPayment}")
    payrollReport.write(f"\nAdmin, {adminTotalPayment}")

    payrollReport.close()


# call exportPayrollReport function and export payroll report to csv file    
exportPayrollReport(employeeList)

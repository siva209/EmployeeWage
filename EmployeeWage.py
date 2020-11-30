#Program to demonstrate store the Employee Daily wages along with Total Wages in List
import random


class EmployeeWage:
    IS_FULL_TIME = 1
    IS_PART_TIME = 2
    empHours = 0
    EMP_WAGE_PER_HOUR = 20
    NUM_OF_WORKING_DAYS = 20
    MAX_HRS_IN_MONTH = 100
    EmployeedailyWages = []

    def checkEmpAttendance(self):
        attendance = random.randint(0, 2)
        if attendance == EmployeeWage.IS_FULL_TIME:
            EmployeeWage.empHours = 8
            print("Employee is present for Full Time")
        elif attendance == EmployeeWage.IS_PART_TIME:
            EmployeeWage.empHours = 4
            print("Employee is present for Part Time")
        else:
            EmployeeWage.empHours = 0
            print("Employee is Absent")

    def calculateMonthlyWages(self):
        totalSalary = 0
        totalEmpHours = 0
        totalWorkingDays = 0
        while totalEmpHours < EmployeeWage.MAX_HRS_IN_MONTH and totalWorkingDays < EmployeeWage.NUM_OF_WORKING_DAYS:
            totalWorkingDays += 1
            self.checkEmpAttendance()
            totalEmpHours += EmployeeWage.empHours
            print(
                f"Days : {totalWorkingDays} and Emp Hours : {EmployeeWage.empHours} and Total Hours : {totalEmpHours}")
            dailyWage = dailyWage = EmployeeWage.EMP_WAGE_PER_HOUR * EmployeeWage.empHours
            print(f"Employee Daily Wage : {dailyWage}")
            EmployeeWage.EmployeedailyWages.append(dailyWage)

        totalSalary = EmployeeWage.EMP_WAGE_PER_HOUR * totalEmpHours
        print("Daily Wages : " + str(EmployeeWage.EmployeedailyWages))
        print(f"Employee Wage for Month is : {totalSalary}")


if __name__ == "__main__":
    employee = EmployeeWage()
    employee.calculateMonthlyWages()

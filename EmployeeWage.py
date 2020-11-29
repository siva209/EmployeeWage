#UC4 using switch case calculate Employee fulltime and part time wages

import random

class EmployeeWage:
 FULL_TIME_HOUR = 8
 PART_TIME_HOUR = 4
 EMPLOYEE_ABSENT = 0
 EMPLOYEE_WAGE_PER_HOUR = 20

 randcheck = random.randint(0, 2)

 def checkEmpAttendance(self):
  if EmployeeWage.randcheck == 1:
   return "Employee is Present for Full Time"
  elif EmployeeWage.randcheck == 2:
   return "Employee is Present for Part Time"
  else:
   return "Employee is Absent"

 def empPerDayHours(self):
  switch = {
   0: EmployeeWage.EMPLOYEE_ABSENT,
   1: EmployeeWage.FULL_TIME_HOUR,
   2: EmployeeWage.PART_TIME_HOUR
  }
  return switch.get(EmployeeWage.randcheck)

 def calculateDailyEmpWage(self, empHours):
  dailyWage = EmployeeWage.EMPLOYEE_WAGE_PER_HOUR * empHours
  return "Employee Daily Wage is : " + str(dailyWage)


if __name__ == "__main__":
 employee = EmployeeWage()
 print(employee.checkEmpAttendance())
 print(employee.calculateDailyEmpWage(employee.empPerDayHours()))
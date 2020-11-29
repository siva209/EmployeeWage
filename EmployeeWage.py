#UC1 checking employee is present r not

import random
class EmployeeWage:

 def checkEmpAttendance(self):
  attendance = random.randint(0, 1)
  if attendance == 1:
   return "Employee is Present"
  else:
   return "Employee is absent"


if __name__ == "__main__":
 employee = EmployeeWage()
 print(employee.checkEmpAttendance())

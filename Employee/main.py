from Employee import Employee

JEFF_KNUPP = Employee('Jeff', 'Knupp', 'S00178', 35000.00, 'HR')
JEFF_KNUPP.display_it()
print() #Adding space in the debug console

JEFF_KNUPP.pay_rise(0.15)
JEFF_KNUPP.display_it()
print()

HAROLD_BEDNTER = Employee('Harold', 'Bendtner', 'S00179', 50000.00, 'Coaching')
HAROLD_BEDNTER.display_it()
print()

Employee.show_count_of_employees()

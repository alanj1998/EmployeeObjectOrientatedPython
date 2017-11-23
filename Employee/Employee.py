class Employee(object):
    """
    The __init__ method is the constructor method
    The properties are declared inside the actual constructor

    Main Learning Things:
            1)Variables and methods follow small case with _ for breaks
            2)Class names use Upper Camelcase
    """
    employee_count = 0

    def __init__(self, first_name, last_name, employee_id, salary, department):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.department = department
        Employee.employee_count += 1

    def display_it(self):
        """
        This method displays the user information

        Main Learning Things:
            1)The print method only accepts strings
            2)In order to round a number we use
                '{0:.2f}'.format(number_to_be_formatted)
        """
        print('Employee ' + self.employee_id)
        print(self.first_name + " " + self.last_name)
        print('Works in the ' + self.department + 
              " department on a basic salary of EUR" + str('{0:.2f}'.format(self.salary)))

    def pay_rise(self, percantage_increase):
        """
        This method adds a pay rise to employees

        Main Learning Things:
            1)Self must be passed to be used
        """
        self.salary = self.salary * (1 + percantage_increase)

    @classmethod
    def show_count_of_employees(cls):
        """
        Static method used to display the amount of Employee objects currently created
        """
        if Employee.employee_count is 1:
            print('There is currently %s Employee created!' % Employee.employee_count)
        else:
            print('There are currently %s Employees created!' % Employee.employee_count)

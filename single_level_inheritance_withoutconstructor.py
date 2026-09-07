class Employee:
    company_name = "Amazon"
    def work_details(self):
        print(f"Employee is working in {Employee.company_name}")
class manager():
    def task(self):
        print(" work of manager is check emp")
obj_e = Employee()
print(dir(obj_e))
obj_m  = manager()
print(dir(obj_m))
obj_e.work_details()
obj_e.task() # attribute error
obj_m.task()
obj_m.workdetails()


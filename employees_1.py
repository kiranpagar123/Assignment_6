import json
class Employee:
    def __init__(self,name,dob,height,city,state):
        self.name=name
        self.dob=dob
        self.height=height
        self.city=city
        self.state=state

    def __str__(self):
        return f"{self.name}, {self.dob}, {self.height}, {self.height}, {self.city}, {self.state}"
    


employee_list=[]

file=open(r"employee.json")
employee_data=json.load(file)

for employee_info in employee_data['employees']:
        name=employee_info['name']
        dob=employee_info['dob']
        height=employee_info['height']
        city=employee_info['city']
        state=employee_info['state']
       
        employee=Employee(name,dob,height,city,state)
        employee_list.append(employee)

for employee in employee_list:
     print(employee)



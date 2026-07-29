class Department:
    def __init__(self, department_id, name, building, head_of_department="None"):
        self.department_id = department_id
        self.name = name
        self.building = building
        self.head_of_department = head_of_department

    def to_dict(self):
        return {
            "department_id": self.department_id,
            "name": self.name,
            "building": self.building,
            "head_of_department": self.head_of_department
        }
        
    def display(self):
        print("=" * 30)
        print("Department ID:", self.department_id)
        print("Name:", self.name)
        print("Building:", self.building)
        print("Head_of_department:", self.head_of_department)
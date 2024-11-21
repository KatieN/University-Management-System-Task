class Person:
    #Sets all the attributes for the class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    #Allows you to re-write the attributes for this class
    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    #Outputs all the attributes for this class
    def get_details(self):
        print("Name: " +self.name+ ", Age: " + str(self.age)+ ", Gender: " + self.gender)

class Student(Person):
    #Sets all the attributes for this class
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender) #Accesses all the attributes from the 'Person' class
        #Adds class-specific attributes
        self.student_id = student_id
        self.course = course
        self.grades= []
    
    #Allows you to re-write the class-specific attributes for this class
    def set_student_details(self, student_id, course):
        self.student_id = student_id
        self.course = course
    
    #Adds a grade to the list of the student's grades
    def add_grade(self, grade):
        self.grades.append(grade)
    
    #Calculates the average grade for the specific student
    def calculate_average_grade(self):
        if len(self.grades) > 0:
            average = sum(self.grades)/len(self.grades)
            #Finds the total sum of all the grades in the list and divides it by the lenght of the list
        else:
            average = 0
        return average
    
    #Outputs all of the attributes for the 'Student' class
    def get_student_summary(self):
        print("Name: " +self.name+ ", Age: " + str(self.age)+ ", Gender: " + self.gender + ", Student ID: " + self.student_id + ", Course: " + self.course + ", Average Grade: " + str(self.average_grade))
    
    def get_mentor(self):
        try: #Tries to set the 'mentor' variable to an attribute 'self.mentor'
            mentor = self.mentor
        except AttributeError: #If this attribute doesn't exist, it instead assigns the mentor variable to "No mentor assigned"
            mentor = "No mentor assigned"
        return mentor

    
class Professor(Person):
    def __init__(self, name, age, gender, staff_id, department, salary):
        super().__init__(name, age, gender)
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
        self.students = []
    
    def set_professor_details(self, staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary
    
    def give_feedback(self, student, feedback):
        print("Feedback for " + student.name + ": " + feedback)
    
    def increase_salary(self, percentage):
        self.salary = self.salary * (1+(percentage/100))
    
    def get_professor_summary(self):
        print("Name: " +self.name+ ", Age: " + str(self.age)+ ", Gender: " + self.gender+ ", Staff ID: " + self.staff_id + ", Department: " + self.department + ", Annual Salary: £" + str("{:.2f}".format(self.salary)))

    def mentor_student(self, student):
        print("Professor " + self.name + " is now mentoring Student " + student.name + " on " + student.course)
        self.students.append(student.name)
        student.mentor = self.name
    
    def get_mentored_students(self):
        print(self.students)

class Administrator(Person):
    def __init__(self, name, age, gender, admin_id, office, years_of_service):
        super().__init__(name, age, gender)
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service
    
    def set_admin_details(self, admin_id, office, years_of_service):
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service
    
    def increment_service_years(self):
        self.years_of_service += 1
    
    def get_admin_summary(self):
        print("Name: " +self.name+ ", Age: " + str(self.age)+ ", Gender: " + self.gender + ", Admin ID: " +self.admin_id+ ", Office: " +self.office+ ", Years Of Service: " + str(self.years_of_service))


alex = Student("Alex", 20 , "Male", "1234", "CS")
katie = Student("Katie", 16, "Female", "6575", "CS")

teacher = Professor("Teacher", 50, "Female", "4321", "CS", 100)
professor = Professor("Professor", 30, "Male", "5756", "History", 200)

admin = Administrator("Admin", 79, "Female", "7978", "Room 12", 16)

alex.add_grade(7)
alex.add_grade(8)
alex.add_grade(9)
alex.average_grade = alex.calculate_average_grade()

katie.average_grade = katie.calculate_average_grade()

teacher.give_feedback(alex, "good job.")
teacher.increase_salary(10)

admin.increment_service_years()

alex.get_student_summary()
katie.get_student_summary()
teacher.get_professor_summary()
professor.get_professor_summary()
admin.get_admin_summary()

professor.mentor_student(alex)

print(alex.get_mentor())

print(katie.get_mentor())

professor.mentor_student(katie)

print(katie.get_mentor())

professor.get_mentored_students()
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class CourseInfo:
    def __init__(self):
        self.num = 0
        self.courses = []

    def num_of_student(self):
        self.num = int(input("Enter number of courses: "))
        return self.num

    def add_course_info(self):
        for student in range(self.num_of_student()):
            c_id = input("ID: ")
            c_name = input("Name: ")
            course = Course(c_id, c_name)
            self.courses.append(course)
        print(f"{self.num} courses has been added")
        return self.courses

    def show_course_info(self):
        print("{:3} | {:10} | {:20} ".format("No.", "ID", "Name"))
        for i in range(len(self.courses)):
            print("{:3} | {:10} | {:20} ".format(str(i+1), self.courses[i].id, self.courses[i].name))

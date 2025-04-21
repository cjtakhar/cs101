
# pset7.py
# CS 101 - Foundations of Data Science and Engineering
# PSET-7: Object Oriented Programming

# Question 1: Student Class
class Student:
    def __init__(self, student_id, major, university):
        self.student_id = student_id
        self.major = major
        self.university = university

# Question 2–9: Project Class with exception handling and full functionality
class Project(Student):
    def __init__(self, student_id, major, university, project_id, data_points):
        super().__init__(student_id, major, university)
        self.project_id = project_id

        if not all(isinstance(x, (int, float)) for x in data_points):
            raise TypeError("All data points must be numerical values (int or float).")

        self.data_points = data_points
        self.__analysis_results = {}
        self.active = True

    def perform_analysis(self):
        try:
            avg = sum(self.data_points) / len(self.data_points)
            self.__analysis_results = {
                "min": min(self.data_points),
                "max": max(self.data_points),
                "avg": avg
            }
        except ZeroDivisionError:
            print("Cannot perform analysis: No data points available.")

    def get_results(self):
        return self.__analysis_results

    def is_active(self):
        return self.active and len(self.data_points) > 0

    def set_active(self, value):
        if not isinstance(value, bool):
            raise TypeError("Active status must be a boolean value.")
        self.active = value

    def add_data(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("New data point must be a numerical value.")
        self.data_points.append(value)

# Question 10: Pandas and OOP Conceptual Question
# ------------------------------------------------
# 1. Class name and parameters used to create df:
#    - Class: pandas.DataFrame
#    - Parameters: data=midterm_scores, columns=['midterm_scores']
#
#    df = pd.DataFrame(midterm_scores, columns=['midterm_scores'])
#
# 2. Attribute being called on df:
#    - df.shape → Returns the shape (rows, columns) of the DataFrame
#
# 3. Method and method parameters used on df:
#    - Method: df.sort_values()
#    - Parameters: by='midterm_scores', ascending=False
#
#    df.sort_values(by='midterm_scores', ascending=False)
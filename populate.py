from connect import engine, db
from models import Program, Course

# program1 = Program(
#     name = "Bachelors in CS",
#     years_of_study = 3
# )

# program2 = Program(
#     name = "Bachelors in Business",
#     years_of_study = 3
# )

#  SAVING PROGRAMS
# db.add_all(
#     [program1,program2]
# )

# db.commit()

# below is as show on video of prior version
# program1 = db.query(Program).filter_by(name = "Bachelors in CS").first()
# *** sqlalchemy 2.0 syntax ***
program1 = db.query(Program).filter(Program.name == "Bachelors in CS").first()

program2 = db.query(Program).filter(Program.name == "Bachelors in Business").first()

course1 = Course(
    title = "Database Management Systems",
    code = "CS 102"
)

course2 = Course(
    title = "Data Science",
    code = "CS 103"
)

course3 = Course(
    title = "Data Structures and Algrithms",
    code = "CS 110"
)

course4 = Course(
    title = "Business Communication",
    code = "BS 123"
)


#  CODE FOR ADDING CHILD OBJECTS TO PARENT
# program1.courses.append(course1)
# program1.courses.append(course2)
# program1.courses.append(course3)
# program2.courses.append(course4)

# db.commit()
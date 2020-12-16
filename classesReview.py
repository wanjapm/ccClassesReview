class Student:
  def __init__(self,name,year):
    self.name = name
    self.year = year
    self.grades = []
    self.attendance = {}

  def __repr__(self):
    return "Student: {} Year:{}\nGrades\n{}Average Score:{:2f}\n".format(self.name,self.year,self.get_grades(),self.get_average())
    
  def add_grade(self,grade):
    if type(grade) == Grade:
      # do not use =='Grade' that will be a string
      self.grades.append(grade)

  def get_average(self):
    sum = 0
    for grade in self.grades:
      sum += grade.score
    return sum / len(self.grades)

  def add_attendance(self,date,status):
    self.attendance[date] = status

  def get_attendance(self,date):
    return self.attendance.get(date,False)

  def get_grades(self):
    grade_str=""
    for grade in self.grades:
      grade_str+= repr(grade)
    return grade_str
  


class Grade:
  minimum_passing = 65
  def __init__(self,score,subject):
    self.score = score
    self.subject = subject

  def __repr__(self):
    return f"{self.subject}:{self.score}. Pass:{self.is_passing()}\n"

  def is_passing(self):
    if self.score >= self.minimum_passing:
      return True
    return False

pieter = Student('Pieter Bruegel the Elder',8)
roger = Student('Roger van der Weyden',10)
sandro = Student('Sandro Botticelli',12)

roger.add_grade(Grade(63,'Maths'))
roger.add_grade(Grade(76,'English'))
roger.add_grade(Grade(54,'Science'))
roger.add_attendance("01/22/2020",True)
roger.add_attendance("01/23/2020",True)
roger.add_attendance("01/24/2020",False)

sandro.add_grade(Grade(92,'Maths'))
sandro.add_grade(Grade(89,'English'))
sandro.add_grade(Grade(84,'Science'))
sandro.add_attendance("01/22/2020",True)
sandro.add_attendance("01/23/2020",False)
sandro.add_attendance("01/24/2020",False)

pieter.add_grade(Grade(100,'Maths'))
pieter.add_grade(Grade(96,'English'))
pieter.add_grade(Grade(88,'Science'))
pieter.add_attendance("01/22/2020",True)
pieter.add_attendance("01/23/2020",True)
pieter.add_attendance("01/24/2020",True)

print(roger)
print(sandro)
print(pieter)
print("=====================")
print(f"Was {roger.name} in attendance on '24 Jan 2020?' : {roger.get_attendance('01/22/2020')}")


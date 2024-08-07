student1={'name':'ali' , 'age' :'20' , 'result' : {'subject' : 'bio' , 'grade': 'B'}}

name = student1['name']
age = student1['age']
subject = student1['result']['subject']
grade = student1['result']['grade']

print(f"The name of student is {name} , his age is {age} , he got {grade} grade in {subject} ")

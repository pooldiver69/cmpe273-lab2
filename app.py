from flask import Flask, escape, request

app = Flask(__name__)

students = list()
classes = list()

@app.route('/')
def hello():
  name = request.args.get("name", "World")
  return f'Hello, {escape(name)}!'

# Create a new student
@app.route('/students', methods = ['POST'])
def createStudent():
  student = request.json
  print(student)
  student['id'] = 123456
  students.append(student)
  return student, 201

# Retrieve an existing student
@app.route('/students/', methods = ['GET'])
def getStudentById():
  id = request.args.get('id', 0)
  id = int(id)
  for student in students:
    if student.get('id') == id:
      return student, 200
  return "cannot find student", 500

# Create a class
@app.route('/classes', methods = ['POST'])
def createClass():
  cla = request.json
  cla['id'] = 1122334
  cla['student'] = []
  classes.append(cla)
  return cla, 201

# Retrieve a class
@app.route('/classes/', methods = ['GET'])
def getClassById():
  id = request.args.get('id', '')
  id = int(id)
  for cla in classes:
    if cla.get('id') == id:
      return cla, 200
  return "cannot find class", 500

# Add students to a class
@app.route('/classes/', methods = ['PATCH'])
def addStudentToClass():
  student = request.json
  student_id = int(student['id'])
  class_id = int(request.args.get('id', ''))
  student_local = None
  print(classes)
  for student in students:
    if student.get('id') == student_id:
      student_local = student
  if student == None:
    return "cannot find student", 500
  for cla in classes:
    if cla.get('id') == class_id:
      cla['student'].append(student_local)
      return cla, 201
  return "cannot find class", 500
  
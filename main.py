from fastapi import FastAPI, Path,HTTPException
import json

app = FastAPI()


def load_data():
    with open('student.json', 'r') as s:
        data = json.load(s)
        return data




@app.get("/")
def hello():
    return "This is the student management system!"
@app.get("/about")
def about():
    return "This is the about page!"


@app.get("/view-students")
def view_students():
    data = load_data()  
    return data 


@app.get("/view-student/{id}")
def view_student_by_id(id: str=Path(..., description="The ID of the student to retrieve",example="STU001")):
    data = load_data()
    for student in data:
        if student["id"] == id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")
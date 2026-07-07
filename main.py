from fastapi import FastAPI
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
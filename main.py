# importing flask class
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import *

# instantiating class flask
app = Flask(__name__)
# this is a config parameter that shows where our database location
app.config.from_object(Development)
# app.config.from_object(Testing)
# app.config.from_object(Production)

db = SQLAlchemy(app)
from models.Employees import EmployeesModel
from models.Departments import DepartmentModel


# TODO:READ MORE ABOUT FLASK-MIGRATE
@app.before_first_request
def create_tables():
    db.create_all()


# registering a route or path
@app.route('/')
# function to run when clients visit this route
def home():
    departments = DepartmentModel.fetch_all()
    print(departments)
    return render_template('index.html', idara=departments)


@app.route('/new_department', methods=['POST'])
def new_department():
    department_name = request.form['department']
    if DepartmentModel.fetch_by_name(department_name):
        # read more on bootstrap alerts with flash
        flash("Department" + department_name + "already exist")
        return redirect(url_for('home'))
    department = DepartmentModel(name=department_name)
    department.insert_to_db()
    return redirect(url_for('home'))


@app.route('/employees/<int:dept_id>')
def employees(dept_id):
    departments = DepartmentModel.fetch_all()
    this_department = DepartmentModel.fetch_by_id(dept_id)
    employees = this_department.employees
    return render_template('employees.html', departments=departments, employees=employees)


@app.route('/payrolls/<int:emp_id>')
def payrolls(emp_id):
    return render_template('payrolls.html')


@app.route('/new_employee', methods=['POST'])
def new_employee():
    full_name = request.form['name']
    gender = request.form['gender']
    kra_pin = request.form['kra_pin']
    email = request.form['email']
    national_id = request.form['national_id']
    basic_salary = request.form['basic_salary']
    benefits = request.form['benefits']
    department_id = int(request.form['dept_id'])

    employee = EmployeesModel(full_name=full_name, gender=gender, KRA_pin=kra_pin, email=email,
                              national_ID=national_id, basic_salary=basic_salary, benefits=benefits,
                              department_id=department_id)
    employee.insert_to_db()
    return redirect(url_for('home'))

# run flask
# if __name__ == '__main__':
#     app.run()

# importing flask class
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from config import *
from resources.payroll import Payroll
import pygal

# instantiating class flask
app = Flask(__name__)
# this is a config parameter that shows where our database location
app.config.from_object(Development)
# app.config.from_object(Testing)
# app.config.from_object(Production)

db = SQLAlchemy(app)
from models.Employees import EmployeesModel
from models.Departments import DepartmentModel
from models.Payrolls import PayrollsModel


# TODO:READ MORE ABOUT FLASK-MIGRATE
@app.before_first_request
def create_tables():
    db.create_all()


# registering a route or path
@app.route('/')
# function to run when clients visit this route
def home():
    departments = DepartmentModel.fetch_all()
    all_employees = EmployeesModel.fetch_all()
    male = 0
    female = 0
    others = 0
    for each in all_employees:
        if each.gender == 'm':
            male += 1
        elif each.gender == 'f':
            female += 1
        else:
            others += 1
    pie_chart = pygal.Pie()
    pie_chart.title = 'Comparing Company Employees by Gender'
    pie_chart.add('Male', male)
    pie_chart.add('Female', female)
    pie_chart.add('Others', others)
    graph = pie_chart.render_data_uri()

    line_chart = pygal.Bar()
    line_chart.title = 'Salary Cost Per Department'
    for each_dept in departments:
        line_chart.add(each_dept.name, DepartmentModel.fetch_total_payroll_by_id(each_dept.id))
    bar_graph = line_chart.render_data_uri()
    # print(graph)
    # print(departments)
    return render_template('index.html', idara=departments, graph=graph, bar_graph=bar_graph)


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
    this_department = DepartmentModel.fetch_by_id(dept_id)
    departments = DepartmentModel.fetch_all()
    return render_template('employees.html', this_department=this_department, idara=departments)


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


@app.route('/edit_employee/<int:id>', methods=['POST'])
def edit_employee(id):
    full_name = request.form['name']
    gender = request.form['gender']
    kra_pin = request.form['kra_pin']
    email = request.form['email']
    national_id = request.form['national_id']
    basic_salary = request.form['basic_salary']
    benefits = request.form['benefits']
    department_id = int(request.form['dept_id'])

    if gender == "na":
        gender = None
    if department_id == "0":
        department_id = None

    EmployeesModel.update_by_id(id=id, full_name=full_name, gender=gender, KRA_pin=kra_pin, email=email,
                                national_ID=national_id, basic_salary=basic_salary, benefits=benefits,
                                department_id=department_id)
    this_emp = EmployeesModel.fetch_by_id(id=id)
    this_dept = this_emp.department
    return redirect(url_for('employees', dept_id=this_dept.id))


@app.route('/deleteEmployee/<int:id>')
def delete_employee(id):
    this_emp = EmployeesModel.fetch_by_id(id=id)
    this_dept = this_emp.department
    EmployeesModel.delete_by_id(id)
    return redirect(url_for('employees', dept_id=this_dept.id))


@app.route('/payrolls/<int:emp_id>')
def payrolls(emp_id):
    employee = EmployeesModel.fetch_by_id(emp_id)
    payslips = PayrollsModel.fetch_by_employee(emp_id)
    return render_template('payrolls.html', employee=employee, payslips=payslips)


@app.route('/generate_payroll/<int:emp_id>', methods=['POST'])
def generate_payrolls(emp_id):
    this_employee = EmployeesModel.fetch_by_id(emp_id)
    payroll = Payroll(this_employee.full_name, this_employee.basic_salary, this_employee.benefits)
    payroll_month = request.form['month']
    overtime = request.form['overtime']
    advanced_pay = request.form['salary_advance']
    loan_deductions = request.form['loan']
    gross = payroll.gross_salary
    nhif = payroll.nhif_deductions
    nssf = round(payroll.nssf_deductions, 2)
    taxable_amount = payroll.taxable_income
    paye = round(payroll.payee, 2)
    personal_relief = payroll.personal_relief
    tax_off_relief = round(payroll.tax_off_relief, 2)
    net_salary = payroll.net_salary
    take_home_pay = net_salary - (float(loan_deductions) + float(advanced_pay))

    payslip = PayrollsModel(payroll_month=payroll_month, overtime=overtime, advanced_pay=advanced_pay,
                            loan_deductions=loan_deductions,
                            gross_salary=gross, nhif_deductions=nhif, nssf_deductions=nssf,
                            taxable_income=taxable_amount,
                            PAYE=paye, personal_relief=personal_relief, tax_off_relief=tax_off_relief,
                            net_salary=net_salary, take_home_pay=take_home_pay)
    payslip.insert_to_db()
    return redirect(url_for('home'))
# run flask
# if __name__ == '__main__':
#     app.run()

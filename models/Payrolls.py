from app import db


class PayrollsModel(db.Model):
    __tablename__ = 'payrolls'
    id = db.Column(db.Integer, primary_key=True)
    payroll_month = db.Column(db.String(50), nullable=False)
    gross_salary = db.Column(db.String(50), unique=True)
    nssf_deductions = db.Column(db.String(50), unique=True, nullable=False)
    PAYE = db.Column(db.Integer, unique=True, nullable=False)
    taxable_income = db.Column(db.Float, nullable=False)
    net_salary = db.Column(db.Float)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

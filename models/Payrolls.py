from main import db


class PayrollsModel(db.Model):
    __tablename__ = 'payrolls'
    id = db.Column(db.Integer, primary_key=True)
    payroll_month = db.Column(db.String(15), nullable=False)
    overtime = db.Column(db.Float)
    advanced_pay = db.Column(db.Float)
    loan_deductions = db.Column(db.Float)
    gross_salary = db.Column(db.Float)
    nssf_deductions = db.Column(db.Float)
    nhif_deductions = db.Column(db.Float)
    taxable_income = db.Column(db.Float)
    PAYE = db.Column(db.Float)
    personal_relief = db.Column(db.Float)
    tax_off_relief = db.Column(db.Float)
    net_salary = db.Column(db.Float)
    take_home_pay = db.Column(db.Float)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_by_employee(cls, emp_id):
        return cls.query.filter_by(employee_id=emp_id)

from main import db


class EmployeesModel(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    KRA_pin = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    national_ID = db.Column(db.String(50), unique=True, nullable=False)
    basic_salary = db.Column(db.Float)
    benefits = db.Column(db.Float)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))



    # create
    def insert_to_db(self):
        db.session.add(self)
        db.session.commit()
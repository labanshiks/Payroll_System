class Payroll:
    name = ""
    basic_salary: int = 0
    benefits: int = 0
    gross_salary: int = 0
    nssf_deductions: int = 0
    nhif_deductions: int = 0
    taxable_income: int = 0
    payee: int = 0
    personal_relief: int = 0
    tax_off_relief: int = 0
    net_salary: int = 0

    def __init__(self, name, basic_salary, benefits):
        Payroll.name = name
        Payroll.basic_salary = basic_salary
        Payroll.benefits = benefits
        Payroll.gross_salary(self)
        Payroll.nhif_deductions(self)
        Payroll.nssf_deductions(self)
        Payroll.taxable_income(self)
        Payroll.payee(self)
        Payroll.personal_relief(self)
        Payroll.tax_off_relief(self)
        Payroll.net_salary(self)

    def gross_salary(self):
        self.gross_salary = self.basic_salary + self.benefits

    def nhif_deductions(self):
        if 0 < self.gross_salary <= 5999:
            self.nhif_deductions = 150
        elif 5999 < self.gross_salary <= 7999:
            self.nhif_deductions = 300
        elif 7999 < self.gross_salary <= 11999:
            self.nhif_deductions = 400
        elif 11999 < self.gross_salary <= 14999:
            self.nhif_deductions = 500
        elif 14999 < self.gross_salary <= 19999:
            self.nhif_deductions = 600
        elif 19999 < self.gross_salary <= 24999:
            self.nhif_deductions = 750
        elif 24999 < self.gross_salary <= 29999:
            self.nhif_deductions = 850
        elif 29999 < self.gross_salary <= 34999:
            self.nhif_deductions = 900
        elif 34999 < self.gross_salary <= 39999:
            self.nhif_deductions = 950
        elif 39999 < self.gross_salary <= 44999:
            self.nhif_deductions = 1000
        elif 44999 < self.gross_salary <= 49999:
            self.nhif_deductions = 1100
        elif 49999 < self.gross_salary <= 59999:
            self.nhif_deductions = 1200
        elif 59999 < self.gross_salary <= 69999:
            self.nhif_deductions = 1300
        elif 69999 < self.gross_salary <= 79999:
            self.nhif_deductions = 1400
        elif 79999 < self.gross_salary <= 89999:
            self.nhif_deductions = 1500
        elif 89999 < self.gross_salary <= 99999:
            self.nhif_deductions = 1600
        else:
            self.nhif_deductions = 1700

    def nssf_deductions(self):
        if self.basic_salary <= 6000:
            self.nssf_deductions = 360
        elif 6000 < self.basic_salary <= 18000:
            self.nssf_deductions = (6 / 100) * self.basic_salary
        else:
            self.nssf_deductions = 1080

    def taxable_income(self):
        self.taxable_income = (self.basic_salary - self.nssf_deductions) + self.benefits

    def payee(self):
        if 0 < self.taxable_income <= 12298:
            self.payee = 0.1 * self.taxable_income
        elif 12298 < self.taxable_income <= 23855:
            self.payee = 1229.80 + (0.15 * (self.taxable_income - 12298))
        elif 23855 < self.taxable_income <= 35472:
            self.payee = 1229.80 + 1733.55 + (0.2 * (self.taxable_income - 23855))
        elif 35472 < self.taxable_income <= 47059:
            self.payee = 1229.80 + 1733.55 + 2323.40 + (0.25 * (self.taxable_income - 35472))
        else:
            self.payee = 1229.80 + 1733.55 + 2323.40 + 2904.25 + (0.3 * (self.taxable_income - 47059))

    def personal_relief(self):
        self.personal_relief = 1408.00

    def tax_off_relief(self):
        self.tax_off_relief = self.payee - self.personal_relief

    def net_salary(self):
        self.net_salary = self.taxable_income - (self.nhif_deductions + self.tax_off_relief)

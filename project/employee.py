# project/employee.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from .models import Employee
from . import db

employee = Blueprint('employee', __name__)

@employee.route('/employees')
@login_required
def employees():
    employees = Employee.query.all()
    return render_template('employees.html', employees=employees)

@employee.route('/employee/create', methods=['GET', 'POST'])
@login_required
def create_employee():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        address = request.form['address']
        phone = request.form['phone']
        salary = request.form['salary']
        department = request.form['department']

        employee = Employee(name=name, gender=gender, address=address, phone=phone, salary=salary, department=department)
        db.session.add(employee)
        db.session.commit()

        flash('Employee created successfully.')
        return redirect(url_for('employee.employees'))

    return render_template('create_employee.html')

@employee.route('/employee/<int:employee_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)

    if request.method == 'POST':
        employee.name = request.form['name']
        employee.gender = request.form['gender']
        employee.address = request.form['address']
        employee.phone = request.form['phone']
        employee.salary = request.form['salary']
        employee.department = request.form['department']

        db.session.commit()

        flash('Employee updated successfully.')
        return redirect(url_for('employee.employees'))

    return render_template('edit_employee.html', employee=employee)

@employee.route('/employee/<int:employee_id>/delete', methods=['POST'])
@login_required
def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()

    flash('Employee deleted successfully.')
    return redirect(url_for('employee.employees'))

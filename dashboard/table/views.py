from django.http import HttpResponse
from django.template import loader
from .forms import EmployeeForm
from reportlab.lib.pagesizes import letter
from .models import Employee  # Adjust based on your actual model name
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfgen import canvas
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.
def main(request):
  template = loader.get_template('tables.html')
  return HttpResponse(template.render())



@login_required
def employee_list(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new employee to the database
            return redirect('employee_list')  # Refresh the page to display the updated data
    else:
        form = EmployeeForm()

    # Retrieve all employees from the database
    employees = Employee.objects.all()

    # Render the template with employee data and the form
    return render(request, 'tables.html', {'employees': employees, 'form': form})



def generate_pdf(request, employee_id):
    # Fetch data from the database based on the user selection (employee)
    employee = Employee.objects.get(id=employee_id)
    
    # Create a response that is a PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="employee_{employee_id}_template.pdf"'

    # Create the PDF with ReportLab
    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Add a title
    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height - 50, "Employee Report")

    # Draw a line under the title
    p.line(50, height - 60, width - 50, height - 60)

    # Add employee details in a structured layout
    data = [
        ["Field", "Value"],  # Table header
        ["Name", f"{employee.firstname} {employee.lastname}"],
        ["Position", employee.position],
        ["Office", employee.office],
        ["Age", employee.age],
        ["Start Date", employee.start_date.strftime("%Y-%m-%d")],
        ["Salary", f"${employee.salary:,.2f}"],
    ]

    # Create a table for the data
    table = Table(data, colWidths=[200, 300])

    # Add styling to the table
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),  # Header background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Align text
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font
        ('FONTSIZE', (0, 0), (-1, -1), 12),  # Font size
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),  # Header padding
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Rows background color
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Table grid
    ]))

    # Add the table to the PDF
    table.wrapOn(p, width, height)
    table.drawOn(p, 80, height - 250)  # Position the table

    # Add footer
    p.setFont("Helvetica", 10)
    p.drawString(50, 30, "Generated with karim's website")
    p.drawRightString(width - 50, 30, f"Employee ID: {employee.id}")

    # Finalize the PDF
    p.showPage()
    p.save()
    
    return response


def test_404(request):
    return render(request, '404.html', status=404)



def register(request):
    if request.method == 'POST':
        print(request.POST)
        # Accessing form data from the request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Debugging prints (remove in production)
        print("First Name:", first_name)
        print("Last Name:", last_name)
        print("Email:", email)
        print("Password:", password)

        # Password confirmation check
        if password != password_confirm:
            return HttpResponse("Passwords do not match.")

        # Create a new user
        try:
            user = User.objects.create_user(
                username=email,  # You can use email or any other identifier
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('login')  # Redirect to the login page after successful registration
        except Exception as e:
            messages.error(request, f"Error: {e}")
    
    return render(request, 'register.html')  # Render the registration page if POST request fails




def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Authenticate user
            user = User.objects.filter(email=email).first()
            print("Password hashed : ", user.password)
            if user.check_password(password):  # Verify hashed password
                print("Well i'm in")
                login(request, user)  # Log the user in
                return redirect('employee_list')  # Redirect to the homepage or dashboard
            else:
                return render(request, 'login.html', {'error': 'Invalid credentials'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'User does not exist'})
    
    return render(request, 'login.html')

def password(request):
    template = loader.get_template('password.html')
    return HttpResponse(template.render())
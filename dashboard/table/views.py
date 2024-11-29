from django.http import HttpResponse
from django.template import loader

from .forms import EmployeeForm
# Create your views here.
def main(request):
  template = loader.get_template('tables.html')
  return HttpResponse(template.render())

from django.shortcuts import render, redirect
from .models import Employee

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


from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import Employee  # Adjust based on your actual model name
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Employee

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

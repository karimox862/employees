# Employee Management Dashboard with PDF Report Generation

This Django-based web application allows users to manage employee data effectively. Key features include:

- **Employee Data Table**: Displays a sortable, searchable table of employees with details such as name, position, office, age, start date, and salary.  
- **Dynamic PDF Generation**: Generate and download customized PDF reports for individual employees, including their detailed information in a professionally formatted layout.  
- **Data Entry Form**: Add new employees through an interactive and user-friendly form, styled using Crispy Forms and Bootstrap.  
- **SQLite Integration**: Employee data is stored and managed using SQLite, ensuring simplicity and scalability for small to medium-sized projects.

## Features in the PDF Report

- Professionally formatted header, table layout, and footer using ReportLab.  
- Dynamic content display with clear formatting for dates, currency, and other fields.  
- Download functionality directly integrated into the data table with a "Download PDF" button.

## Password Reset Feature

As part of improving user authentication, I have added a **Password Reset** feature. The feature includes the following pages:

- **Password Reset Request Page**: Users can request a password reset by entering their email address.
- **Password Reset Email**: A link is sent to the user's email to reset the password.
- **Password Reset Confirmation Page**: After clicking the link, users can enter and confirm their new password.

Here are some images of the password reset pages:

### Password Reset Request Page:
![reset password](https://github.com/user-attachments/assets/2c8c4352-8016-4aaf-9e8f-0ca8a94b318f)


### Password Reset Email:
![email sent](https://github.com/user-attachments/assets/271a4578-3f5d-4c65-9196-25fe8fa4164e)


### Password Reset Confirmation Page:
![new password](https://github.com/user-attachments/assets/f7b497c4-9bf6-47f7-84a6-fa54c1c9a4ae)


## Technologies Used

- **Backend**: Django with SQLite  
- **Frontend**: Bootstrap and DataTables.js  
- **PDF Generation**: ReportLab library for custom, dynamic report creation.

## Usage

1. Clone the repository, set up the environment, and migrate the database.  
2. The application provides an interactive dashboard for managing employees, adding new entries, and generating PDF reports with a single click.

## Future Improvements

- Enhanced styling for the employee table and forms.  
- Support for additional file formats (e.g., Excel, CSV).  
- Role-based access control for managing employee data.


![Screenshot from 2024-12-01 21-51-58](https://github.com/user-attachments/assets/92c8669d-8ed6-4029-b5df-113c59c20030)


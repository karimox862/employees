Employee Management Dashboard with PDF Report Generation

This Django-based web application allows users to manage employee data effectively. Key features include:

Employee Data Table: Displays a sortable, searchable table of employees with details such as name, position, office, age, start date, and salary.
Dynamic PDF Generation: Generate and download customized PDF reports for individual employees, including their detailed information in a professionally formatted layout.
Data Entry Form: Add new employees through an interactive and user-friendly form, styled using Crispy Forms and Bootstrap.
SQLite Integration: Employee data is stored and managed using SQLite, ensuring simplicity and scalability for small to medium-sized projects.

Features in the PDF Report

Professionally formatted header, table layout, and footer using ReportLab.
Dynamic content display with clear formatting for dates, currency, and other fields.
Download functionality directly integrated into the data table with a "Download PDF" button.

Technologies Used

Backend: Django with SQLite
Frontend: Bootstrap and DataTables.js
PDF Generation: ReportLab library for custom, dynamic report creation.

Usage

Clone the repository, set up the environment, and migrate the database. The application provides an interactive dashboard for managing employees, adding new entries, and generating PDF reports with a single click.
Future Improvements

Enhanced styling for the employee table and forms.
Support for additional file formats (e.g., Excel, CSV).
Role-based access control for managing employee data.

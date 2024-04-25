import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from CRUDFunctions import *
from Gpa import *

# Login function
def login():
    user_id = "1234"
    password = "pass"
    
    if (user_id_entry.get() == user_id) and (password_entry.get() == password):
        text_var.set("Connected")
        login_frame.pack_forget()  # Hide the login frame
        switch_to_tab_view()
    else:
        text_var.set("Wrong password or user ID")

# Switch to tab view function
def switch_to_tab_view():
    tab_view.pack(padx=20, pady=20)

# Create Student function
def create_student():
    # Get student information
    student_id = student_id_entry.get()
    student_name = student_name_entry.get()
    student_email = student_email_entry.get()
    student_school = student_school_entry.get()
    student_program = student_program_entry.get()
    
    # Call CreateStudent function with the retrieved information
    CreateStudent(student_id, student_name, student_email, student_school, student_program)

# Calculate GPA function
def calculate_gpa():
    # Get credits and grade points entered by the user
    credits = float(credits_entry.get())
    grade_points = float(grade_entry.get())
    
    # Calculate GPA using the CalculateGpa function
    gpa = CalculateGpa([credits], [grade_points])  # Pass as lists
    gpa_label.configure(text="GPA: {:.2f}".format(gpa))

# Generate report function
def generate_report():
    # Function to generate report for at-risk students
    # Implement your report generation logic here
    report_text.configure(state=tk.NORMAL)
    report_text.delete(1.0, tk.END)
    report_text.insert(tk.END, "Report generated for at-risk students:\n")
    # Add at-risk student details to the report
    report_text.insert(tk.END, "Student ID: 123456, Name: John Doe, GPA: 1.8\n")
    report_text.insert(tk.END, "Student ID: 789012, Name: Jane Smith, GPA: 1.9\n")
    report_text.configure(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Academic Probation Alert System")

# Login Page
login_frame = ctk.CTkFrame(master=root, width=300, height=300, corner_radius=10)
login_frame.pack(padx=40, pady=40)

user_id_entry = ctk.CTkEntry(master=login_frame, placeholder_text="USER ID", width=150, height=30, border_width=2, corner_radius=10)
user_id_entry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="PASSWORD", width=150, height=30, show="*", border_width=2, corner_radius=10)
password_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

login_button = ctk.CTkButton(master=login_frame, text="LOG IN", command=login)
login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

text_var = tk.StringVar()
login_label = ctk.CTkLabel(master=login_frame, textvariable=text_var, width=120, height=25, fg_color=("white","black"), corner_radius=8)
login_label.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

# Tab View Page (Initially hidden)
tab_view = ctk.CTkTabview(root)

create_student_tab = tab_view.add("Add Student")
calculate_gpa_tab = tab_view.add("Calculate GPA")
view_results_tab = tab_view.add("Report")

# Create Student Page
create_student_frame = ctk.CTkFrame(master=create_student_tab, width=500, height=300, corner_radius=10)
create_student_frame.pack(padx=40, pady=40, expand=True, fill=tk.BOTH)

student_id_entry = ctk.CTkEntry(master=create_student_frame, placeholder_text="Student ID", width=300, height=30, border_width=2, corner_radius=10)
student_id_entry.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

student_name_entry = ctk.CTkEntry(master=create_student_frame, placeholder_text="Student Name", width=300, height=30, border_width=2, corner_radius=10)
student_name_entry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

student_email_entry = ctk.CTkEntry(master=create_student_frame, placeholder_text="Student Email", width=300, height=30, border_width=2, corner_radius=10)
student_email_entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

student_school_entry = ctk.CTkEntry(master=create_student_frame, placeholder_text="Student School", width=300, height=30, border_width=2, corner_radius=10)
student_school_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

student_program_entry = ctk.CTkEntry(master=create_student_frame, placeholder_text="Student Program", width=300, height=30, border_width=2, corner_radius=10)
student_program_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Submit Button
submit_button = ctk.CTkButton(master=create_student_frame, text="Submit", command=create_student)
submit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Calculate GPA Page (Modified to match Create Student design)
calculate_gpa_frame = ctk.CTkFrame(master=calculate_gpa_tab, width=500, height=300, corner_radius=10)
calculate_gpa_frame.pack(padx=40, pady=40)

credits_label = ctk.CTkLabel(master=calculate_gpa_frame, text="Credits:", width=120, height=25)
credits_label.place(relx=0.3, rely=0.2, anchor=tk.CENTER)

credits_entry = ctk.CTkEntry(master=calculate_gpa_frame, width=150, height=30, border_width=2, corner_radius=10)
credits_entry.place(relx=0.6, rely=0.2, anchor=tk.CENTER)

grade_label = ctk.CTkLabel(master=calculate_gpa_frame, text="Grade Points:", width=120, height=25)
grade_label.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

grade_entry = ctk.CTkEntry(master=calculate_gpa_frame, width=150, height=30, border_width=2, corner_radius=10)
grade_entry.place(relx=0.6, rely=0.4, anchor=tk.CENTER)

calculate_button = ctk.CTkButton(master=calculate_gpa_frame, text="Calculate GPA", command=calculate_gpa)
calculate_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

gpa_label = ctk.CTkLabel(master=calculate_gpa_frame, text="GPA: -", width=120, height=25)
gpa_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# View Results Page
report_button = ttk.Button(view_results_tab, text="Generate Report", command=generate_report)
report_button.pack(padx=10, pady=10)

report_text = tk.Text(view_results_tab, height=10, width=50)
report_text.pack(padx=10, pady=10)
report_text.configure(state=tk.DISABLED)

# Run the GUI
root.mainloop()
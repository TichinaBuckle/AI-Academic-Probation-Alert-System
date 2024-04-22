import customtkinter
import tkinter

def switch_to_tab_view():
    tabView.pack(padx=20, pady= 20)  # Show the tab view page

def switch_to_login_page():
    tabView.pack_forget()  # Hide the tab view page

def login():
    if (user_id_entry.get() == user_id) and (password_entry.get() == password):
        text_var.set("Connected")
        switch_to_tab_view()  # Call function to switch to the tab view page
    else:
        text_var.set("Wrong password or user ID")

def create_student():
    # Get ID number and name from entry fields
    student_id = student_id_entry.get()
    student_name = student_name_entry.get()
    
    # Do something with the student ID and name (for example, print them)
    print("Student ID:", student_id)
    print("Student Name:", student_name)

# Create main window
app = customtkinter.CTk()
app.title("Academic Probation")
app.geometry("1000x800")

# Login Page
login_frame = customtkinter.CTkFrame(master=app, width=300, height=300, corner_radius=10)
login_frame.pack(padx=40, pady=40)

user_id_entry = customtkinter.CTkEntry(master=login_frame, placeholder_text="ID NUMBER", width=150, height=30, border_width=2, corner_radius=10)
user_id_entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

password_entry = customtkinter.CTkEntry(master=login_frame, placeholder_text="PASSWORD", width=150, height=30, show="*", border_width=2, corner_radius=10)
password_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

user_id = "1802146"
password = "BROWN64"

login_button = customtkinter.CTkButton(master=login_frame, text="LOG IN", command=login)
login_button.place(relx=0.5 ,rely=0.6, anchor=tkinter.CENTER)

text_var = tkinter.StringVar()

login_label = customtkinter.CTkLabel(master=login_frame, textvariable=text_var, width=120, height=25, fg_color=("white","black"), corner_radius=8)
login_label.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

# Tab View Page (Initially hidden)
tabView = customtkinter.CTkTabview(app)

create_student_tab = tabView.add("Create Student")
calculate_gpa_tab = tabView.add("Calculate GPA")
view_results_tab = tabView.add("View Results")

# Create Student Page
create_student_frame = customtkinter.CTkFrame(master=create_student_tab, width=300, height=300, corner_radius=10)
create_student_frame.pack(padx=40, pady=40)

student_id_entry = customtkinter.CTkEntry(master=create_student_frame, placeholder_text="Student ID", width=150, height=30, border_width=2, corner_radius=10)
student_id_entry.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

student_name_entry = customtkinter.CTkEntry(master=create_student_frame, placeholder_text="Student Name", width=150, height=30, border_width=2, corner_radius=10)
student_name_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

create_button = customtkinter.CTkButton(master=create_student_frame, text="CREATE STUDENT", command=create_student)
create_button.place(relx=0.5 ,rely=0.6, anchor=tkinter.CENTER)

app.mainloop()



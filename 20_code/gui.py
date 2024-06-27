import mysql.connector
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.ttk import Button
from tkinter import messagebox
import pandas as pd

# Create Window
root = Tk()
root.attributes('-fullscreen', True)
root.title('Ignite Data Analysis Tool')

# Create Tags
tagsLabel = Label(root, text="Tags:").grid(row=0, column=0)

class Dropdown:
    def __init__(self, master, options, button_label, row):
        self.master = master
        self.options = options
        self.selected_options = []

        self.button_label = button_label
        self.dropdown_button = Button(master, text=self.button_label, command=self.show_dropdown)
        self.dropdown_button.grid(row=row, column=0)

        self.dropdown_window = None

    def show_dropdown(self):
        if self.dropdown_window is None:
            self.dropdown_window = Toplevel(self.master)
            self.dropdown_window.wm_title("Select Options")
            self.dropdown_window.geometry("200x200")
            self.dropdown_window.transient(self.master)
            self.dropdown_window.grab_set()
            self.dropdown_window.protocol("WM_DELETE_WINDOW", self.on_dropdown_close)

            self.listbox = Listbox(self.dropdown_window, selectmode='multiple')
            self.listbox.pack(expand=True, fill='both')

            for option in self.options:
                self.listbox.insert(END, option)

            select_button = Button(self.dropdown_window, text="Select", command=self.select_options)
            select_button.pack()

    def select_options(self):
        self.selected_options = [self.listbox.get(i) for i in self.listbox.curselection()]
        selected_text = ", ".join(self.selected_options)

        if self.selected_options:
            self.dropdown_button.config(text=selected_text)
        else:
            self.dropdown_button.config(text=self.button_label)
        
        self.dropdown_window.destroy()
        self.dropdown_window = None

    def on_dropdown_close(self):
        self.dropdown_window.destroy()
        self.dropdown_window = None

genderoptions = ["Male", "Female", "All Genders"]
genderdropdown = Dropdown(root, genderoptions, "Gender", 1)

gradeoptions = ["6", "7", "8", "9", "10", "11", "12", "All Grades"]
gradedropdown = Dropdown(root, gradeoptions, "Grade", 2)

schooloptions = ["Public (Including DPS)", "DPS", "Private"]
schooldropdown = Dropdown(root, schooloptions, "School Type", 3)

zipcodeoptions = ["00000", "11111"]
zipcodedropdown = Dropdown(root, zipcodeoptions, "Zip Code", 4)

curriculumoptions = ["Light", "Water", "Health"]
curriculumdropdown = Dropdown(root, curriculumoptions, "Learner Curriculum", 5)

studenttypeoptions = ["Learner", "Maker", "Trainer"]
studenttypedropdown = Dropdown(root, studenttypeoptions, "Student Type", 6)

programyearoptions = ["2021-2022", "2022-2023", "2023-2024"]
programyeardropdown = Dropdown(root, programyearoptions, "Program Year", 7)

studentcontinuationoptions = ["1 year Learner", "2 year Learner", "3 year Learner", "Learner to Maker", "1 year Maker", "2 year Maker", "3 year Maker"]
studentcontinuationdropdown = Dropdown(root, studentcontinuationoptions, "Student Continuation", 8)

class Checkbox:
    def __init__(self, root, text, row):
        self.var = IntVar()
        self.c = Checkbutton(root, text=text, variable=self.var)
        self.c.grid(row=row, column=1)

checkbox1 = Checkbox(root, "Visualization", 1)
checkbox2 = Checkbox(root, "Engagement Scores", 2)
checkbox3 = Checkbox(root, "Attendance Percentage", 3)
checkbox4 = Checkbox(root, "Paired t-test", 4)
checkbox5 = Checkbox(root, "ANOVA", 5)

operationsLabel = Label(root, text="Operations:").grid(row=0, column=1)

def query_database(query, params):
    try:
        connection = mysql.connector.connect(
            host='ignite',
            user='root',
            password='ignite',
            database='ignite_database'
        )
        print("Connected to the database")
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        print("Data retrieved successfully")
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def generate_visualization():
    selected_genders = genderdropdown.selected_options
    selected_grades = gradedropdown.selected_options
    selected_schools = schooldropdown.selected_options
    selected_zipcodes = zipcodedropdown.selected_options
    selected_curriculums = curriculumdropdown.selected_options
    selected_student_types = studenttypedropdown.selected_options
    selected_program_years = programyeardropdown.selected_options
    selected_student_continuations = studentcontinuationdropdown.selected_options

    if not selected_student_types:
        messagebox.showerror("Error", "Please select a valid student type")
        return

    # Determine the table and column names based on the selected student type
    if 'Learner' in selected_student_types:
        table_name = 'learners'
        grade_column = 'Grade'
        gender_column = 'Gender'
        school_column = 'School'
        zipcode_column = 'Zipcode'
        curriculum_column = 'Curriculum'
        program_year_column = 'Year'
        student_continuation_column = 'student_continuation'
    elif 'Maker' in selected_student_types:
        table_name = 'makers'
        grade_column = 'Grade'
        gender_column = 'Gender'
        school_column = 'School'
        zipcode_column = 'Zipcode'
        curriculum_column = 'Curriculum'
        program_year_column = 'Year'
        student_continuation_column = 'student_continuation'
    else:
        # Handle other cases or show an error
        messagebox.showerror("Error", "Please select a valid student type")
        return

    # Building the query dynamically based on selected options
    query = f"SELECT {grade_column}, {gender_column}, {school_column}, {zipcode_column}, {curriculum_column}, {program_year_column}, {student_continuation_column} FROM {table_name} WHERE 1=1"
    params = []

    if selected_genders:
        query += f" AND {gender_column} IN ({','.join(['%s'] * len(selected_genders))})"
        params.extend(selected_genders)
    if selected_grades:
        query += f" AND {grade_column} IN ({','.join(['%s'] * len(selected_grades))})"
        params.extend(selected_grades)
    if selected_schools:
        query += f" AND {school_column} IN ({','.join(['%s'] * len(selected_schools))})"
        params.extend(selected_schools)
    if selected_zipcodes:
        query += f" AND {zipcode_column} IN ({','.join(['%s'] * len(selected_zipcodes))})"
        params.extend(selected_zipcodes)
    if selected_curriculums:
        query += f" AND {curriculum_column} IN ({','.join(['%s'] * len(selected_curriculums))})"
        params.extend(selected_curriculums)
    if selected_program_years:
        query += f" AND {program_year_column} IN ({','.join(['%s'] * len(selected_program_years))})"
        params.extend(selected_program_years)
    if selected_student_continuations:
        query += f" AND {student_continuation_column} IN ({','.join(['%s'] * len(selected_student_continuations))})"
        params.extend(selected_student_continuations)

    # Log the query and parameters for debugging
    print(f"Query: {query}")
    print(f"Parameters: {params}")

    data = query_database(query, params)

    # Print the retrieved data for debugging
    print(f"Retrieved data: {data}")

    # For visualization
    if data:
        columns = ["Grade", "Gender", "School", "Zipcode", "Curriculum", "Year", "StudentContinuation"]
        df = pd.DataFrame(data, columns=columns)
        
        # Filter the dataframe for columns starting with 'avg_diff_'
        avg_diff_columns = [col for col in df.columns if col.startswith('avg_diff_')]
        
        if avg_diff_columns:
            avg_diff_means = df[avg_diff_columns].mean()
            avg_diff_means.plot(kind='bar')
            plt.title('Average Differences by Tags')
            plt.xlabel('Tags')
            plt.ylabel('Average Difference')
            plt.show()
        else:
            messagebox.showerror("Error", "No columns starting with 'avg_diff_' found")
    else:
        messagebox.showerror("Error", "Failed to retrieve data from the database")

generate_button = Button(root, text="Generate Visualization", command=generate_visualization)
generate_button.grid(row=7, column=1)

root.mainloop()

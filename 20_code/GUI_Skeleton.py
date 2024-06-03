from tkinter import *
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter.ttk import Button

# Create Window
root = Tk()
root.title('Ignite Data Analysis Tool')
root.geometry("400x400")

# Create Tags
tagsLabel = Label(root, text="Tags:").grid(row=0, column=0)

class GenderDropdown:
    def __init__(self, master, options, button_label="Gender"):
        self.master = master
        self.options = options
        self.selected_options = []

        # Initial label for the dropdown button
        self.button_label = button_label
        # Create a Button widget to trigger the dropdown, and pack it
        self.dropdown_button = Button(master, text=self.button_label, command=self.show_dropdown)
        self.dropdown_button.grid(row=1, column=0)

        # Initialize the dropdown window as None
        self.dropdown_window = None

    def show_dropdown(self):
        # Check if the dropdown window is already created
        if self.dropdown_window is None:
            # Create a new Toplevel window for the dropdown
            self.dropdown_window = Toplevel(self.master)
            self.dropdown_window.wm_title("Select Options")
            self.dropdown_window.geometry("200x200")
            # Set the dropdown window to be transient (always on top of the parent window)
            self.dropdown_window.transient(self.master)
            # Make the dropdown window modal
            self.dropdown_window.grab_set()

            # Create a Listbox widget for displaying options, with multiple selection mode
            self.listbox = Listbox(self.dropdown_window, selectmode='multiple')
            self.listbox.pack(expand=True, fill='both')

            # Insert options into the Listbox
            for option in self.options:
                self.listbox.insert(END, option)

            # Create a Button to confirm the selections and pack it
            select_button = Button(self.dropdown_window, text="Select", command=self.select_options)
            select_button.pack()

    def select_options(self):
        # Get the selected options from the Listbox
        self.selected_options = [self.listbox.get(i) for i in self.listbox.curselection()]
        selected_text = ", ".join(self.selected_options)

        # Update the dropdown button text with the selected options
        if self.selected_options:
            self.dropdown_button.config(text=selected_text)
        else:
            self.dropdown_button.config(text=self.button_label)
        
        # Destroy the dropdown window and reset the reference to None
        self.dropdown_window.destroy()
        self.dropdown_window = None

# List of options to display in the dropdown
genderoptions = ["Male", "Female", "All Genders"]
# Create an instance of the GenderDropdown class
genderdropdown = GenderDropdown(root, genderoptions)

class GradeDropdown:
    def __init__(self, master, options, button_label="Grade"):
        self.master = master
        self.options = options
        self.selected_options = []

        # Initial label for the dropdown button
        self.button_label = button_label
        # Create a Button widget to trigger the dropdown, and pack it
        self.dropdown_button = Button(master, text=self.button_label, command=self.show_dropdown)
        self.dropdown_button.grid(row=2, column=0)

        # Initialize the dropdown window as None
        self.dropdown_window = None

    def show_dropdown(self):
        # Check if the dropdown window is already created
        if self.dropdown_window is None:
            # Create a new Toplevel window for the dropdown
            self.dropdown_window = Toplevel(self.master)
            self.dropdown_window.wm_title("Select Options")
            self.dropdown_window.geometry("200x200")
            # Set the dropdown window to be transient (always on top of the parent window)
            self.dropdown_window.transient(self.master)
            # Make the dropdown window modal
            self.dropdown_window.grab_set()

            # Create a Listbox widget for displaying options, with multiple selection mode
            self.listbox = Listbox(self.dropdown_window, selectmode='multiple')
            self.listbox.pack(expand=True, fill='both')

            # Insert options into the Listbox
            for option in self.options:
                self.listbox.insert(END, option)

            # Create a Button to confirm the selections and pack it
            select_button = Button(self.dropdown_window, text="Select", command=self.select_options)
            select_button.pack()

    def select_options(self):
        # Get the selected options from the Listbox
        self.selected_options = [self.listbox.get(i) for i in self.listbox.curselection()]
        selected_text = ", ".join(self.selected_options)

        # Update the dropdown button text with the selected options
        if self.selected_options:
            self.dropdown_button.config(text=selected_text)
        else:
            self.dropdown_button.config(text=self.button_label)
        
        # Destroy the dropdown window and reset the reference to None
        self.dropdown_window.destroy()
        self.dropdown_window = None
gradeoptions = ["6", "7", "8", "9", "10", "11", "12"]
gradedropdown = GradeDropdown(root, gradeoptions)

class SchoolDropdown:
    def __init__(self, master, options, button_label="School Type"):
        self.master = master
        self.options = options
        self.selected_options = []

        # Initial label for the dropdown button
        self.button_label = button_label
        # Create a Button widget to trigger the dropdown, and pack it
        self.dropdown_button = Button(master, text=self.button_label, command=self.show_dropdown)
        self.dropdown_button.grid(row=3, column=0)

        # Initialize the dropdown window as None
        self.dropdown_window = None

    def show_dropdown(self):
        # Check if the dropdown window is already created
        if self.dropdown_window is None:
            # Create a new Toplevel window for the dropdown
            self.dropdown_window = Toplevel(self.master)
            self.dropdown_window.wm_title("Select Options")
            self.dropdown_window.geometry("200x200")
            # Set the dropdown window to be transient (always on top of the parent window)
            self.dropdown_window.transient(self.master)
            # Make the dropdown window modal
            self.dropdown_window.grab_set()

            # Create a Listbox widget for displaying options, with multiple selection mode
            self.listbox = Listbox(self.dropdown_window, selectmode='multiple')
            self.listbox.pack(expand=True, fill='both')

            # Insert options into the Listbox
            for option in self.options:
                self.listbox.insert(END, option)

            # Create a Button to confirm the selections and pack it
            select_button = Button(self.dropdown_window, text="Select", command=self.select_options)
            select_button.pack()

    def select_options(self):
        # Get the selected options from the Listbox
        self.selected_options = [self.listbox.get(i) for i in self.listbox.curselection()]
        selected_text = ", ".join(self.selected_options)

        # Update the dropdown button text with the selected options
        if self.selected_options:
            self.dropdown_button.config(text=selected_text)
        else:
            self.dropdown_button.config(text=self.button_label)
        
        # Destroy the dropdown window and reset the reference to None
        self.dropdown_window.destroy()
        self.dropdown_window = None
schooloptions = ["Public (Including DPS)", "DPS", "Private"]
schooldropdown = SchoolDropdown(root, schooloptions)

class ZipCodeDropdown:
    def __init__(self, master, options, button_label="Zip Code"):
        self.master = master
        self.options = options
        self.selected_options = []

        # Initial label for the dropdown button
        self.button_label = button_label
        # Create a Button widget to trigger the dropdown, and pack it
        self.dropdown_button = Button(master, text=self.button_label, command=self.show_dropdown)
        self.dropdown_button.grid(row=4, column=0)

        # Initialize the dropdown window as None
        self.dropdown_window = None

    def show_dropdown(self):
        # Check if the dropdown window is already created
        if self.dropdown_window is None:
            # Create a new Toplevel window for the dropdown
            self.dropdown_window = Toplevel(self.master)
            self.dropdown_window.wm_title("Select Options")
            self.dropdown_window.geometry("200x200")
            # Set the dropdown window to be transient (always on top of the parent window)
            self.dropdown_window.transient(self.master)
            # Make the dropdown window modal
            self.dropdown_window.grab_set()

            # Create a Listbox widget for displaying options, with multiple selection mode
            self.listbox = Listbox(self.dropdown_window, selectmode='multiple')
            self.listbox.pack(expand=True, fill='both')

            # Insert options into the Listbox
            for option in self.options:
                self.listbox.insert(END, option)

            # Create a Button to confirm the selections and pack it
            select_button = Button(self.dropdown_window, text="Select", command=self.select_options)
            select_button.pack()

    def select_options(self):
        # Get the selected options from the Listbox
        self.selected_options = [self.listbox.get(i) for i in self.listbox.curselection()]
        selected_text = ", ".join(self.selected_options)

        # Update the dropdown button text with the selected options
        if self.selected_options:
            self.dropdown_button.config(text=selected_text)
        else:
            self.dropdown_button.config(text=self.button_label)
        
        # Destroy the dropdown window and reset the reference to None
        self.dropdown_window.destroy()
        self.dropdown_window = None
zipcodeoptions = ["00000",  "11111"]
zipcodedropdown = ZipCodeDropdown(root, zipcodeoptions)

class CurriculumDropdown:
    def __init__(self, master, options, button_label="Learner Curriculum"):
        self.master = master
        self.options = options
        self.selected_options = []

        # Initial label for the dropdown button
        self.button_label = button_label
        # Create a Button widget to trigger the dropdown, and pack it
        self.dropdown_button = Button(master, text=self.button_label, command=self.show_dropdown)
        self.dropdown_button.grid(row=5, column=0)

        # Initialize the dropdown window as None
        self.dropdown_window = None

    def show_dropdown(self):
        # Check if the dropdown window is already created
        if self.dropdown_window is None:
            # Create a new Toplevel window for the dropdown
            self.dropdown_window = Toplevel(self.master)
            self.dropdown_window.wm_title("Select Options")
            self.dropdown_window.geometry("200x200")
            # Set the dropdown window to be transient (always on top of the parent window)
            self.dropdown_window.transient(self.master)
            # Make the dropdown window modal
            self.dropdown_window.grab_set()

            # Create a Listbox widget for displaying options, with multiple selection mode
            self.listbox = Listbox(self.dropdown_window, selectmode='multiple')
            self.listbox.pack(expand=True, fill='both')

            # Insert options into the Listbox
            for option in self.options:
                self.listbox.insert(END, option)

            # Create a Button to confirm the selections and pack it
            select_button = Button(self.dropdown_window, text="Select", command=self.select_options)
            select_button.pack()

    def select_options(self):
        # Get the selected options from the Listbox
        self.selected_options = [self.listbox.get(i) for i in self.listbox.curselection()]
        selected_text = ", ".join(self.selected_options)

        # Update the dropdown button text with the selected options
        if self.selected_options:
            self.dropdown_button.config(text=selected_text)
        else:
            self.dropdown_button.config(text=self.button_label)
        
        # Destroy the dropdown window and reset the reference to None
        self.dropdown_window.destroy()
        self.dropdown_window = None
curriculumoptions = ["Light", "Water", "Health"]
curriculumdropdown = CurriculumDropdown(root, curriculumoptions)

class StudentTypeDropdown:
    def __init__(self, master, options, button_label="Student Type"):
        self.master = master
        self.options = options
        self.selected_options = []

        # Initial label for the dropdown button
        self.button_label = button_label
        # Create a Button widget to trigger the dropdown, and pack it
        self.dropdown_button = Button(master, text=self.button_label, command=self.show_dropdown)
        self.dropdown_button.grid(row=6, column=0)

        # Initialize the dropdown window as None
        self.dropdown_window = None

    def show_dropdown(self):
        # Check if the dropdown window is already created
        if self.dropdown_window is None:
            # Create a new Toplevel window for the dropdown
            self.dropdown_window = Toplevel(self.master)
            self.dropdown_window.wm_title("Select Options")
            self.dropdown_window.geometry("200x200")
            # Set the dropdown window to be transient (always on top of the parent window)
            self.dropdown_window.transient(self.master)
            # Make the dropdown window modal
            self.dropdown_window.grab_set()

            # Create a Listbox widget for displaying options, with multiple selection mode
            self.listbox = Listbox(self.dropdown_window, selectmode='multiple')
            self.listbox.pack(expand=True, fill='both')

            # Insert options into the Listbox
            for option in self.options:
                self.listbox.insert(END, option)

            # Create a Button to confirm the selections and pack it
            select_button = Button(self.dropdown_window, text="Select", command=self.select_options)
            select_button.pack()

    def select_options(self):
        # Get the selected options from the Listbox
        self.selected_options = [self.listbox.get(i) for i in self.listbox.curselection()]
        selected_text = ", ".join(self.selected_options)

        # Update the dropdown button text with the selected options
        if self.selected_options:
            self.dropdown_button.config(text=selected_text)
        else:
            self.dropdown_button.config(text=self.button_label)
        
        # Destroy the dropdown window and reset the reference to None
        self.dropdown_window.destroy()
        self.dropdown_window = None
studenttypeoptions = ["Learner", "Maker", "Trainer"]
studenttypedropdown = StudentTypeDropdown(root, studenttypeoptions)

class ProgramYearDropdown:
    def __init__(self, master, options, button_label="Program Year"):
        self.master = master
        self.options = options
        self.selected_options = []

        # Initial label for the dropdown button
        self.button_label = button_label
        # Create a Button widget to trigger the dropdown, and pack it
        self.dropdown_button = Button(master, text=self.button_label, command=self.show_dropdown)
        self.dropdown_button.grid(row=7, column=0)

        # Initialize the dropdown window as None
        self.dropdown_window = None

    def show_dropdown(self):
        # Check if the dropdown window is already created
        if self.dropdown_window is None:
            # Create a new Toplevel window for the dropdown
            self.dropdown_window = Toplevel(self.master)
            self.dropdown_window.wm_title("Select Options")
            self.dropdown_window.geometry("200x200")
            # Set the dropdown window to be transient (always on top of the parent window)
            self.dropdown_window.transient(self.master)
            # Make the dropdown window modal
            self.dropdown_window.grab_set()

            # Create a Listbox widget for displaying options, with multiple selection mode
            self.listbox = Listbox(self.dropdown_window, selectmode='multiple')
            self.listbox.pack(expand=True, fill='both')

            # Insert options into the Listbox
            for option in self.options:
                self.listbox.insert(END, option)

            # Create a Button to confirm the selections and pack it
            select_button = Button(self.dropdown_window, text="Select", command=self.select_options)
            select_button.pack()

    def select_options(self):
        # Get the selected options from the Listbox
        self.selected_options = [self.listbox.get(i) for i in self.listbox.curselection()]
        selected_text = ", ".join(self.selected_options)

        # Update the dropdown button text with the selected options
        if self.selected_options:
            self.dropdown_button.config(text=selected_text)
        else:
            self.dropdown_button.config(text=self.button_label)
        
        # Destroy the dropdown window and reset the reference to None
        self.dropdown_window.destroy()
        self.dropdown_window = None
programyearoptions = ["2021-2022", "2022-2023", "2023-2024" ]
programyeardropdown = ProgramYearDropdown(root, programyearoptions)

class StudentContinuationDropdown:
    def __init__(self, master, options, button_label="Student Continuation"):
        self.master = master
        self.options = options
        self.selected_options = []

        # Initial label for the dropdown button
        self.button_label = button_label
        # Create a Button widget to trigger the dropdown, and pack it
        self.dropdown_button = Button(master, text=self.button_label, command=self.show_dropdown)
        self.dropdown_button.grid(row=8, column=0)

        # Initialize the dropdown window as None
        self.dropdown_window = None

    def show_dropdown(self):
        # Check if the dropdown window is already created
        if self.dropdown_window is None:
            # Create a new Toplevel window for the dropdown
            self.dropdown_window = Toplevel(self.master)
            self.dropdown_window.wm_title("Select Options")
            self.dropdown_window.geometry("200x200")
            # Set the dropdown window to be transient (always on top of the parent window)
            self.dropdown_window.transient(self.master)
            # Make the dropdown window modal
            self.dropdown_window.grab_set()

            # Create a Listbox widget for displaying options, with multiple selection mode
            self.listbox = Listbox(self.dropdown_window, selectmode='multiple')
            self.listbox.pack(expand=True, fill='both')

            # Insert options into the Listbox
            for option in self.options:
                self.listbox.insert(END, option)

            # Create a Button to confirm the selections and pack it
            select_button = Button(self.dropdown_window, text="Select", command=self.select_options)
            select_button.pack()

    def select_options(self):
        # Get the selected options from the Listbox
        self.selected_options = [self.listbox.get(i) for i in self.listbox.curselection()]
        selected_text = ", ".join(self.selected_options)

        # Update the dropdown button text with the selected options
        if self.selected_options:
            self.dropdown_button.config(text=selected_text)
        else:
            self.dropdown_button.config(text=self.button_label)
        
        # Destroy the dropdown window and reset the reference to None
        self.dropdown_window.destroy()
        self.dropdown_window = None
studentcontinuationoptions = ["1 year Learner", "2 year Learner", "3 year Leaner", "Learner to Maker", "1 year Maker", "2 year Maker", "3 year Maker"]
studentcontinuationdropdown = StudentContinuationDropdown(root, studentcontinuationoptions)


# Run the Tkinter event loop
root.mainloop()

#testing to see if git works



# Create Operations
operationsLabel = Label(root, text= "Operations:").grid(row=0, column=2)





root.mainloop()
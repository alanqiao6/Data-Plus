# Data-Plus
Ignite: Improving Students’ STEM-Identity Through Design and Tinkering
Ignite Data Analysis Tool: ignitebass.pythonanywhere.com

---
# Ignite Data Analysis Tool
## API
The API is hosted on pythonanywhere.com with front-end in HTML and Javascript and back-end in Flask and Python.
Data stored in /home/igniteBass/db/ignite.sql , Python code in /home/igniteBass/flask/gui.py and HTML/Javascript code in /home/igniteBass/flask/templates/index.html.


## Updating Dataset
Prerequisites: Install MySQLWorkbench and compile deidentified dataset into .csv file with column names in the form of finalguidataset.csv using the Python Data Dictionary to translate the column names from the questions in the pre and post surveys.

Run database.py with file path to dataset, export the file from MySQLWorkbench and save as ignite.sql, and upload file to /home/igniteBass/db/ignite.sql on PythonAnywhere. 
On PythonAnywhere, enter the MySQL: igniteBass$data console and use SOURCE db/ignite.sql;

Reload the website to use the new dataset.

---

## PythonAnywhere Maintenance
PythonAnywhere must be reloaded on the Web tab every 3 months to keep the website running.

---

## Google Drive
Includes our presentation slides/video, visualizations, data dictionary, and data analysis.

---

## DukeBox
Includes all original pre and post survey question results labeled by each year. Also includes engagement scores, registration, and other relevant data.

---

## Github
Github hosts our original data, clean data (scrubbed and deidentified), and code. You can access our various datasets in final and score datasets, with final_gui_dataset in 50_score_datasets being the dataset used in our API.

The code section includes how we manipulated the dataset in python and R to create our final_gui_dataset. This final_gui_dataset includes all survey questions with scores across learners, makers, and trainers, along with added columns such as student_continuation.

---

# Final Datasets Creation

## Makers
Includes information from 2022 and 2023. It groups the databases in the following specific order:
- 🗂️ **Makers Application**
- 📝 **Pre Survey**
- 📊 **Post Survey**

## Learners
Includes information from 2021, 2022, and 2023. It groups the databases in the following specific order:
- 📋 **Learners Registration**
- 📚 **Roster**
- 📝 **Pre Survey**
- 📊 **Post Survey**

---

It is important to note that, for example, in the case of Learners, different questions were asked each year, which may not be included in all years. Therefore, for columns such as `Season`, `Wk1 Style`, or `Health: I would be willing to join community heart and lung health initiatives, such as volunteer opportunities`, there will not be responses for all years. 

For a detailed view of these columns, please refer to the file named **"Column comparison"** located in the folder **"40_finalDatasets"**.

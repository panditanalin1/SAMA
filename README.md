# SAMA — Student Academic & Marks Analyzer

SAMA (which is a command-line program based on Python) is designed to calculate and provide a summary of a student's academic marks.

The student's name, number of subjects, maximum marks, names of the subjects, and marks are entered as input; the program deals with this information and produces an academic report which includes the total, average, percentage, and subjects in which the student scored the highest and the lowest.

It is a Python project aimed at beginners and shows how to use variables, input and output, lists, loops, conditional statements, and basic mathematical operations.

---

## Project Components

This project contains three main components:

```text
SAMA/
│
├── SAMA.py
├── README.md
└── project_report.pdf
```

### 1. SAMA.py

The main Python program is `SAMA.py`.

It contains the complete logic of SAMA, including:

* Taking student information as input
* Taking subject names and marks
* Storing the entered information
* Calculating the total marks
* Calculating the average marks
* Calculating percentage
* Finding the highest marks
* Finding the lowest marks
* Identifying the subjects with the highest and lowest marks
* Displaying the final academic report in form of percentage,average marks,highest and lowest scoring subject
*The Grades are not provided in order to let the student introspect on themselves and encourage themselves to be better 

### 2. README.md

The file describes the project and gives instructions on how to install or run it.

It is presented in such a way that a person who has never used the project can learn how to run it.

### 3. project_report.pdf

Here is the detailed project report for SAMA.

The text outlines the project's purpose, aims, method of operation, design, implementation, results, and other relevant details.

---

# Features

SAMA currently provides the following features:

* Student name input
* Multiple subject support
* Marks input for each subject
* Total marks calculation
* Average marks calculation
* Percentage calculation
* Highest-scoring subject identification
* Lowest-scoring subject identification
* Simple command-line academic report

---

# Requirements

To run SAMA, you need:

* Python 3.x
* A computer with a command-line/terminal
* No external Python libraries are required

Since the program makes use of Python's built-in features, there is no need for a pip install step.

---

# Installation

## Step 1 — Install Python

If Python isn't already installed on your computer, then you should download and install Python 3 from the official Python website.

After installation, open a terminal or command prompt and check whether Python is installed:

```bash
python --version
```

If that command does not work, try:

```bash
python3 --version
```

You ought to see the version number for Python 3.

---

## Step 2 — Get the Project

Get or clone this repository.

Using Git:

```bash
git clone
```

Then move into the project folder:

```bash
cd SAMA
```

When you have downloaded the project in the form of a ZIP file, you should extract it and then open the `SAMA` folder that has been extracted in your terminal.

---

# How to Run the Project

Ensure that you are in the folder that contains the file `SAMA.py`.

Run:

```bash
python SAMA.py
```

If your computer uses `python3` instead, run:

```bash
python3 SAMA.py
```

The terminal will be where the program starts.

---

# How the Program Works

SAMA adopts a simple approach consisting of Input → Process → Output.

### 1. Input

The program first asks for:

* Student name
* Number of subjects
* Maximum marks
* Subject names
* Marks obtained in each subject

For example:

```text
Enter student name: Rahul

Enter number of subjects: 3

Enter Maximum marks for the exam: 50

Enter subject name: Mathematics

Enter marks for subject: 42

Enter subject name: Python

Enter marks for subject: 46

Enter subject name: English

Enter marks for subject: 40
```

### 2. Processing

On receipt of the input, SAMA carries out the marking.

It calculates:

**Total Marks**

```text
Total = sum of all subject marks
```

**Average Marks**

```text
Average = Total Marks / Number of Subjects
```

**Percentage**

```text
Percentage = (Average Marks / Maximum Marks) × 100
```

The program also determines the highest and lowest marks and names the subjects to which they correspond.

### 3. Output

Once the information has been processed, SAMA produces an academic report.

Example:

```text
~===== ACADEMIC REPORT =====~

Student: Rahul

Mathematics : 42

Python : 46

English : 40

Total Marks: 128

Average Marks: 42.666666666666664

Percentage: 85.33333333333333 %

Highest Scoring Subject is: Python

Least Scoring Subject is : English
```

The precise output will vary according to the data entered by the user.

---

# Program Flow

The basic flow of SAMA is:

```text
Start

↓

Enter Student Information

↓

Enter Number of Subjects

↓

Enter Maximum Marks

↓

Enter Subject Names and Marks

↓

Store Marks and Subjects

↓

Calculate Total

↓

Calculate Average

↓

Calculate Percentage

↓

Find Highest and Lowest Marks

↓

Display Academic Report

↓

End
```

---

# Python Concepts Used

The project demonstrates several basic Python concepts:

### Variables

Information such as the student's name, the number of subjects, the marks, the total, the average, and the percentage is stored using variables.

### Input and Output

The function `input()` is used for obtaining information from the user, and `print()` is used for displaying the results.

### Lists

Lists are used for storing subject names and marks.

```python
subjects = []

marks = []
```

### Loops

The user is repeatedly asked for subject names and marks using a `for` loop.

### Built-in Functions

The project uses built-in Python functions such as:

```python
sum()

max()

min()
```

They are employed for working out the total and for determining both the highest and lowest marks.

### Conditional Statements

The use of `if` statements is to determine which subject corresponds to the highest and lowest marks.

---

# Project Structure

```text
SAMA/
│
├── SAMA.py
│  └── Main Python program
│
├── README.md
│  └── Project documentation and instructions
│
└── project_report.pdf
   └── Detailed project report
```

---

# Running the Project in VS Code

If you are using Visual Studio Code:

1. Open Visual Studio Code.

2. Click File, then choose Open Folder.

3. Chose the SAMA project folder.

4. Open `SAMA.py`.

5. Open the VS Code terminal.

6. Run:

```bash
python SAMA.py
```

7. Input the required information into the terminal.

8. The academic report won't be shown until all the inputs have been entered.

---

# Limitations

The present version of SAMA has been deliberately made simple.

It achieves this via the command line.

The results you enter are not stored permanently.

It does not use a database.

It doesn't feature a graphical user interface.

At the moment it is concentrating on the analysis of basic marks.

---

# Future Improvements

Possible future improvements include:

* Adding automatic grade calculation
* Saving academic reports to a file
* Adding graphical representations of marks
* Adding attendance analysis
* Adding more detailed performance analysis
* Creating a graphical user interface

---

# Conclusion

SAMA is an academic marks analysis program which has been developed using Python.

The project shows the way in which basic programming ideas such as variables, lists, loops, conditional statements, user input, and built-in functions can be put together to deal with a practical problem.

The aim of the project is to make it simple enough for a person new to the subject to understand at the same time giving a useful example of a full Python command-line application.

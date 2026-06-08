# Data Analyzer and Transformer Program

A menu-driven Python application that allows users to input, analyze, filter, sort, and perform calculations on numerical datasets. The program demonstrates the use of Python fundamentals such as lists, functions, recursion, lambda functions, built-in functions, and pattern matching (`match-case`).

---

## Features

### 1. Input Data

* Accepts a one-dimensional array of integers from the user.
* Stores the dataset for further operations.

<img width="1388" height="431" alt="image" src="https://github.com/user-attachments/assets/9e603347-9ca6-46d9-b037-31bf4c6f1636" />


### 2. Display Data Summary

Displays:

* Total number of elements
* Maximum value
* Minimum value
* Sum of all values
* Average value

Uses Python built-in functions:

* `len()`
* `max()`
* `min()`
* `sum()`

<img width="1388" height="452" alt="image" src="https://github.com/user-attachments/assets/7ff5375c-b0b6-434d-b27f-2fae083d4844" />


### 3. Calculate Factorial (Recursion)

* Calculates the factorial of a user-entered number.
* Uses a recursive function implementation.

Example:

Factorial of 5 = 120

<img width="1393" height="339" alt="Screenshot 2026-06-09 005355" src="https://github.com/user-attachments/assets/06a1ba5d-a6ed-4e59-b542-b9640bf8a768" />


### 4. Filter Data by Threshold (Lambda Function)

* Filters dataset values greater than or equal to a threshold value.
* Implemented using a lambda function and list comprehension.

Example:

Dataset: [10, 20, 30, 40]
Threshold: 25
Output: 30,40

<img width="1394" height="357" alt="Screenshot 2026-06-09 005418" src="https://github.com/user-attachments/assets/c917db4c-fc85-4207-a3e9-d8d5325ec6de" />


### 5. Sort Data

Provides two sorting options:

* Ascending Order
* Descending Order

Uses:

* `list.sort()`
* `list.sort(reverse=True)`

<img width="1392" height="671" alt="Screenshot 2026-06-09 005454" src="https://github.com/user-attachments/assets/cf195c11-9bf1-45f7-b141-81f7dfaa061f" />


### 6. Display Dataset Statistics

Displays:

* Maximum Value
* Minimum Value
* Sum of Values
* Average Value

<img width="1386" height="400" alt="Screenshot 2026-06-09 005519" src="https://github.com/user-attachments/assets/6df8faa8-856d-414a-a877-1bd6ab6bf3f0" />


### 7. Exit Program

Terminates the application safely.

<img width="1383" height="313" alt="Screenshot 2026-06-09 005543" src="https://github.com/user-attachments/assets/3f3583c6-7cc9-43db-b805-9a6621274422" />


---

## Concepts Demonstrated

* Lists
* List Comprehensions
* Lambda Functions
* Recursive Functions
* Built-in Functions
* Pattern Matching (`match-case`)
* Loops (`while`)
* Conditional Statements
* User Input Handling

---

## Requirements

* Python 3.10 or higher

The program uses the `match-case` statement which was introduced in Python 3.10.

---

## How to Run

### Clone or Download the Project

```bash
git remote add origin https://github.com/Dhruvvv0320/Project-4_Functional_Treat.git
```

### Navigate to the Project Directory

```bash
cd Project_4
```

### Run the Program

```bash
python Functional_Treat.py
```

---

## Sample Execution

```text
Welcome to the Data Analyzer and Transformer Program

Main Menu :
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program

Enter your choice : 1

Enter Data for a 1D array (separated by spaces):
10 20 30 40 50

Data has been stored successfully...
```

---

## Project Structure

```text
Project_4/
│
├── Functional_Treat.py
├── README.md
```

---

## Future Improvements

* Add median and mode calculations.
* Support floating-point numbers.
* Save and load datasets from files.
* Add graphical visualization using Matplotlib.
* Implement error handling for invalid inputs.
* Support multiple datasets.

---

## Author

Developed as a Python practice project to demonstrate data manipulation, recursion, lambda functions, sorting, and menu-driven programming.

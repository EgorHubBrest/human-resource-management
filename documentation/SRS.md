# Human Resource Management

## Introduction

### Purpose

«Human Resource Management» is web-application which allows users to view and modify information about departments and employees. 

## Overall description

### Product features

Application should provide:
* Storing information about departments and employees in database;
* Display list of departments;
* Sorting list of departments by alphabet;
* Updating the list of departments (editing, adding, removing);
* Display list of all employees;
* Filtering by department for employees;
* Updating the list of employees (editing, adding, removing).

## System features

## 1. Home page

When the user launches the application he is taken to the Home page where he can select a table.
User can go to the home page by clicking on “Human Resource Management”.

![Pic 1. Home page.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/1.png)

_Pic 1. Home page._

## 2. Departments

### 2.1 Display list of departments

The mode is designed to view the list of departments and their names. 

__*Main scenario:*__

* User select item “Departments” on Home page;
* Application displays list of departments.

![Pic 2.1 View the departments list.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/21.png)

_Pic 2.1 View the departments list._

The list displays all departments names and average salary in each department. 


### 2.2 Sorting by alphabet

Sorting by alphabet is available.

__*Main scenario:*__

* In the departments list view mode, user select radio button “Sort by alphabet”;
* The application will display sorted departments list.


### 2.3 Search

Search is available.

__*Main scenario:*__

*	User enters in “Search” field department name;
*	The application will display appropriate departments list.


### 2.4 Add department

__*Main scenario:*__

* User clicks the “Add department” button in the departments list view mode;
* Application displays form to enter department name;
* User enters department name and presses “Add department” button;
* If error occurs, then error message is displaying;
* If new department record is successfully added, then list of departments with added records is displaying.

__*Cancel operation scenario:*__

* User clicks the “Add department” button in the departments list view mode;
* Application displays form to enter department data;
* User enters department name and presses “Cancel” button;
* Data don’t save in data base, then list of departments is displaying to user.
* If the user selects the menu item "Departments” or "Employees", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Pic 2.2 Add department](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/22.png)

_Pic 2.2 Add department_

When adding a department, only department name is entered.

If error occurs, then error message is displaying.

![Pic 2.3 Error of adding department.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/23.png)

_Pic 2.3 Error of adding department._


### 2.5 Edit department

__*Main scenario:*__

* User clicks the “Edit” button (picture with pencil) in the departments list view mode;
* Application displays form to edit department name;
* User enters department name and presses “Edit department” button;
* If error occurs, then error message is displaying;
* If department record is successfully edited, then list of departments with added records is displaying.


__*Cancel operation scenario:*__

* User clicks the “Edit ” button in the departments list view mode;
* Application displays form to enter department data;
* User enters department name and presses “Cancel” button;
* Data don’t save in data base, then list of departments is displaying to user.
* If the user selects the menu item "Departments” or "Employees", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Pic 2.4 Edit department.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/24.png)

_Pic 2.4 Edit department._

When editing a department, only department name is entered.

Constraints for department name validation:
* maximum length of 70 characters;
* cannot enter the name of an existing department.

If error occurs, then error message is displaying.

![Pic 2.5 Error of editing department.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/25.png)

_Pic 2.5 Error of editing department._


### 2.5 Removing department

__*Main scenario:*__

* The user, while in the list of departments, presses the "Delete" button in the selected department line;
* If the department can be removed, application displays confirmation dialog “Are you sure you want to delete this department?”;
* The user confirms the removal of the department;
* Record is deleted from database;
* If error occurs, then error message displays;
* If department record is successfully deleted, then list of departments without deleted records is displaying.

__*Cancel operation scenario:*__

* The user, while in the list of departments, presses the "Delete" button in the selected department line;
* If the department can be removed, application displays confirmation dialog “Are you sure you want to delete this department?”;
* User press “Cancel” button;
* List of orders without changes is displaying.

![Pic 2.6 Removing department.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/26.png)

_Pic 2.6 Removing department._

If error occurs, then error message is displaying.

![Pic 2.7 Error of removing department.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/27.png)

_Pic 2.7 Error of removing department._

If department is not empty, then following message is displaying.

![Pic 2.8 Empty department removing.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/28.png)

_Pic 2.8 Empty department removing._


## 3. Employees

### 3.1 Display list of employees

This mode is intended for viewing and editing the employees list.

__*Main scenario:*__

* User select item «Employees»;
* Application displays list of employees.

![Pic 3.1 View the employee list.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/31.png)

_Pic 3.1 View the employee list._

The list displays following columns:

* Related department – department where the employee works;
* Employee name – employee’s first name and last name;
* Date of birth – employee’s date of birth;
* Salary – employee’s salary.


### 3.2 Sorting by department

Sorting by department is available.

__*Main scenario:*__

* In the employee list view mode, user select radio button “Sort by department”;
* The application will display sorted appropriate departments list.


### 3.3 Sorting by name

Sorting by name is available.

__*Main scenario:*__

* In the employee list view mode, user select radio button “Sort by name”;
* The application will display sorted appropriate departments list.


### 3.4 Sorting by salary

Sorting by salary is available.

__*Main scenario:*__

* In the employee list view mode, user select radio button “Sort by salary”;
* The application will display sorted appropriate departments list.


### 3.5 Filtering by department:

Filtering by date of birth is available.

__*Main scenario:*__

* In the employees list view mode, the user selects a department with combo “Select department” and presses the “Show” button;
* The application will show the employees only from selected department.


### 3.6 Add employee:

__*Main scenario:*__

* User clicks the “Add employee” button in the employees list view mode;
* Application displays form to enter employee’s data;
* User enters employee’s data and presses “Add employee” button;
* If entered data is valid, then record is adding to database;
* If error occurs, then error message is displaying;
* If new employee record is successfully added, then list of employees with added records is displaying.

__*Cancel operation scenario:*__

* User clicks the “Add employee” button in the employees list view mode;
* Application displays form to enter employee data;
* User enters employee’s data and presses “Cancel” button;
* Data don’t save in data base, then list of employees is displaying to user.
* If the user selects the menu item "Departments” or "Employees", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Pic 3.2 Add employee.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/32.png)

_Pic 3.2 Add employee._

__*When adding an employee, the following details are entered:*__

* Related department – department where the employee works;
* Employee name – employee’s first name and last name;
* Date of birth – employee’s date of birth;
* Salary – employee’s salary.

__*Constraints for data validation:*__

* Related department – user select existing department;
* Employee name – employee’s first name and last name;
* Date of birth – date in format dd/mm/yyyy;
* Salary – positive float number.

If error occurs, then error message displays:

![Pic 3.3 Error of adding department.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/33.png)

_Pic 3.3 Error of adding department._


### 3.7 Edit employee

__*Main scenario:*__

* User clicks the “Edit employee” button in the employees list view mode;
* Application displays form to edit employee’s data;
* User enters employee’s data and presses “Edit employee” button; 
* If entered data is valid, then edited record is adding to database;
* If error occurs, then error message is displaying;
* If employee record is successfully edited, then list of employees with edited records is displaying.

__*Cancel operation scenario:*__

* User clicks the “Edit employee” button in the employees list view mode;
* Application displays form to enter employee data;
* User enters employee data and presses “Cancel” button;
* Data don’t save in data base, then list of employees is displaying to user.
* If the user selects the menu item "Departments” or "Employees", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Pic 3.4 Edit employee.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/34.png)

_Pic 3.4 Edit employee._

If error occurs, then error message displays:

![Pic 3.5 Error of editing department.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/35.png)

_Pic 3.5 Error of editing department._


### 3.8 Removing employee

__*Main scenario:*__

* The user, while in the list of employees, presses the "Delete" button in the selected emplyee line;
* If the employee can be removed, application displays confirmation dialog “Are you sure you want to delete this employee?”;
* The user confirms the removal of the employee;
* Record is deleted from database;
* If error occurs, then error message displays;
* If employee record is successfully deleted, then list of employees without deleted records is displaying.

__*Cancel operation scenario:*__

* The user, while in the list of employees, presses the "Delete" button in the selected employee line;
* If the employee can be removed, application displays confirmation dialog “Are you sure you want to fire this employee?”;
* User press “Cancel” button;
* List of orders without changes is displaying.

![Pic 3.6 Delete employee.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/36.png)

_Pic 3.6 Delete employee._

If error occurs, then error message displays:

![Pic 3.7 Error of remowing department.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/37.png)

_Pic 3.7 Error of removing department._

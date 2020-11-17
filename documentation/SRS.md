# Human Resource Management
## Vision

«Human Resource Management» is web-application which allows users to view and modify information about departments and employees. 

Application should provide:
* Storing information about departments and employees in database;
* Display list of departments;
* Sorting list of departments by alphabet;
* Updating the list of departments (editing, adding, removing);
* Display list of all employees;
* Filtering by department for employees;
* Updating the list of employees (editing, adding, removing).
 
## 1. Departments
    
### 1.1 Display list of departments
   
The mode is designed to view the list of departments and their names. Sorting by alphabet is available.

__*Main scenario:*__

* User select item "Departments";
* Application displays list of departments.

![Pic 1.1 View the departments list.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/11.png)

_Pic 1.1 View the departments list._

The list displays all departments names. 

__*Sorting by alphabet:*__

* In the departments list view mode, user select radio button “Sort by alphabet”;
* The application will display sorted departments list.


### 1.2 Add department

__*Main scenario:*__

* User clicks the “Add” button in the departments list view mode;
* Application displays form to enter department name;
* User enters department name and presses “Save” button;
* If entered data is valid, then record is adding to database;
* If error occurs, then error message is displaying;
* If entered department name exists in table, then error message is displaying;
* If new department record is successfully added, then list of departments with added records is displaying.

__*Cancel operation scenario:*__

* User clicks the “Add” button in the departments list view mode;
* Application displays form to enter department data;
* User enters department name and presses “Cancel” button;
* Data don’t save in data base, then list of departments is displaying to user.
* If the user selects the menu item "Departments” or "Employees", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Pic 1.2 Add department](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/12.png)

_Pic 1.2 Add department_

When adding a department, only department name is entered.


### 1.3 Edit department

__*Main scenario:*__

* User clicks the “Edit” button in the departments list view mode;
* Application displays form to edit department name;
* User enters department name and presses “Save” button;
* If entered data is valid, then edited record is adding to database;
* If error occurs, then error message is displaying;
* If department record is successfully edited, then list of departments with added records is displaying.

__*Cancel operation scenario:*__

* User clicks the “Edit ” button in the departments list view mode;
* Application displays form to enter department data;
* User enters department name and presses “Cancel” button;
* Data don’t save in data base, then list of departments is displaying to user.
* If the user selects the menu item "Departments” or "Employees", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Pic 1.3 Edit department.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/13.png)

_Pic 1.3 Edit department._

When editing a department, only department name is entered.

Constraints for department name validation:
* maximum length of 70 characters;


### 1.4 Removing department

__*Main scenario:*__

* The user, while in the list of departments, presses the "Delete" button in the selected department line;
* If the department can be removed, application displays confirmation dialog “Are you sure you want to delete this department?”;
* The user confirms the removal of the department;
* Record is deleted from database;
* If error occurs, then error message displays;
* If department record is successfully deleted, then list of departments without deleted records is displaying.

__*Cancel operation scenario:*__

* The user, while in the list of departments, presses the "Delete" button in the selected department line;
* If the department can be removed, application displays confirmation dialog “Are you sure you want to delete this department?”;
* User press “Cancel” button;
* List of orders without changes is displaying.

![Pic 1.4 Removing department dialog.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/14.png)

_Pic 1.4 Removing department dialog._


## 2. Employees

### 2.1 Display list of employees

This mode is intended for viewing and editing the employees list.

__*Main scenario:*__

* User select item «Employees»;
* Application displays list of employees.

![Pic 2.1 View the employee list.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/21.png)

_Pic 2.1 View the employee list._

The list displays following columns:

* Related department – department where the employee works;
* Employee name – employee’s first name and last name;
* Date of birth – employee’s date of birth;
* Salary – employee’s salary.

__*Filtering by department:*__

* In the employees list view mode, the user selects a department with combo “Select department” and presses the “Show” button;
* The application will show the employees only from selected department.


### 2.2 Add employee:

__*Main scenario:*__

* User clicks the “Add” button in the employees list view mode;
* Application displays form to enter employee’s data;
* User enters employee’s data and presses “Save” button;
* If entered data is valid, then record is adding to database;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If error occurs, then error message is displaying;
* If new employee record is successfully added, then list of employees with added records is displaying.

__*Cancel operation scenario:*__

* User clicks the “Add” button in the employees list view mode;
* Application displays form to enter employee data;
* User enters employee’s data and presses “Cancel” button;
* Data don’t save in data base, then list of employees is displaying to user.
* If the user selects the menu item "Departments” or "Employees", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Pic 2.2 Add employee.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/22.png)

_Pic 2.2 Add employee._

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


### 2.3 Edit employee

__*Main scenario:*__

* User clicks the “Edit” button in the employees list view mode;
* Application displays form to edit employee’s data;
* User enters employee’s data and presses “Save” button;
* If any data is entered incorrectly, incorrect data messages are displayed;
* If entered data is valid, then edited record is adding to database;
* If error occurs, then error message is displaying;
* If employee record is successfully edited, then list of employees with added records is displaying.

__*Cancel operation scenario:*__

* User clicks the “Edit ” button in the employees list view mode;
* Application displays form to enter employee data;
* User enters employee data and presses “Cancel” button;
* Data don’t save in data base, then list of employees is displaying to user.
* If the user selects the menu item "Departments” or "Employees", the data will not be saved to the database and the corresponding form with updated data will be opened.

![Pic 2.3 Edit employee.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/23.png)

_Pic 2.3 Edit employee._


### 2.4 Removing employee

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

![Pic 2.4 Delete employee dialog.](https://github.com/krisstinkou/human-resource-management/blob/dev/documentation/images/24.png)

_Pic 2.4 Delete employee dialog._

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

_*Main scenario:*_

* User select item “Departments”;
* Application displays list of departments.

![Pic 1.1 View the departments list.](/home/chris/work/SRS/11.png)

Pic 1.1 View the departments list.

The list displays all departments names. 

_*Sorting by alphabet:*_

* In the departments list view mode, user select radio button “Sort by alphabet”;
* The application will display sorted departments list.

### 1.2 Add department

_*Main scenario:*_

* User clicks the “Add” button in the departments list view mode;
* Application displays form to enter department name;
* User enters department name and presses “Save” button;
* If entered data is valid, then record is adding to database;
* If error occurs, then error message is displaying;
* If entered department name exists in table, then error message is displaying;
* If new department record is successfully added, then list of departments with added records is displaying.

_*Cancel operation scenario:*_

* User clicks the “Add” button in the departments list view mode;
* Application displays form to enter department data;
* User enters department name and presses “Cancel” button;
* Data don’t save in data base, then list of departments is displaying to user.
* If the user selects the menu item "Departments” or "Employees", the data will not be saved to the database and the corresponding form with updated data will be opened.

Pic 1.2 Add department

When adding a department, only department name is entered.

### 1.3 Edit department

_*Main scenario:*_

* User clicks the “Edit” button in the departments list view mode;
* Application displays form to edit department name;
* User enters department name and presses “Save” button;
* If entered data is valid, then edited record is adding to database;
* If error occurs, then error message is displaying;
* If department record is successfully edited, then list of departments with added records is displaying.

_*Cancel operation scenario:*_

* User clicks the “Edit ” button in the departments list view mode;
* Application displays form to enter department data;
* User enters department name and presses “Cancel” button;
* Data don’t save in data base, then list of departments is displaying to user.
* If the user selects the menu item "Departments” or "Employees", the data will not be saved to the database and the corresponding form with updated data will be opened.

Pic 1.3 Edit department.

When editing a department, only department name is entered.

Constraints for department name validation:
* maximum length of 70 characters;

### 1.4 Removing department

_*Main scenario:*_

* The user, while in the list of departments, presses the "Delete" button in the selected department line;
* If the department can be removed, application displays confirmation dialog “Are you sure you want to delete this department?”;
* The user confirms the removal of the department;
* Record is deleted from database;
* If error occurs, then error message displays;
* If department record is successfully deleted, then list of departments without deleted records is displaying.

_*Cancel operation scenario:*_

* The user, while in the list of departments, presses the "Delete" button in the selected department line;
* If the department can be removed, application displays confirmation dialog “Are you sure you want to delete this department?”;
* User press “Cancel” button;
* List of orders without changes is displaying.

Pic 1.4 Removing department dialog.


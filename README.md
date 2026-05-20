# Hospital-Management-System
#**Project Title**
**Hospital Management System Using PySide6**

##**Research Problem**
Managing patient records manually can be slow, unorganized, and prone to errors. This project aims to create a simple desktop application to manage patient information efficiently using a graphical user interface.

##**Motivation**
The motivation of this project is to learn GUI development using Python and PySide6 while building a practical real-world application. It also helps improve skills in programming, user interaction, and data handling.

##**Control Flow**
1. The application starts and displays the main window.
2. The user enters patient information into input fields.
3. Clicking **Add** stores the data and updates the table.
4. Clicking **Delete** removes the selected patient record.
5. The `refresh()` function updates the table after every change.
   
##**Implementation Strategy**
The project was developed using **Python** and **PySide6**.
The application uses:
* `QLineEdit` for text inputs
* `QPushButton` for Add/Delete actions
* `QTableWidget` to display patient records

import sys
from PySide6.QtWidgets import *

class App(QWidget):
    def __init__(self):
        super().__init__()

        #WINDOW SETTINGS
        self.setWindowTitle("Hospital App")  # Window title
        self.resize(700, 400)  # Window size

        #DATA STORAGE
        # This list stores all patients temporarily
        self.data = []

        #MAIN LAYOUT (VERTICAL)
        layout = QVBoxLayout()

        self.inputs = []  # list to store all input fields

        for text in ["Name", "Age", "Gender", "Doctor", "Appointment"]:
            inp = QLineEdit()  # creates a text input box
            inp.setPlaceholderText(text)  # hint text inside box 

            self.inputs.append(inp)  # save input in list
            layout.addWidget(inp)    # add input to UI

        # BUTTON SECTION

        # ADD BUTTON → adds patient data to list
        btn_add = QPushButton("Add")

        # DELETE BUTTON → removes selected row from table
        btn_del = QPushButton("Delete")

        # Connect buttons to functions
        btn_add.clicked.connect(self.add)       # when clicked → run add()
        btn_del.clicked.connect(self.delete)    # when clicked → run delete()

        # Add buttons to layout
        layout.addWidget(btn_add)
        layout.addWidget(btn_del)

        # TABLE (SHOWS ALL PATIENTS)
        self.table = QTableWidget()

        # 5 columns = Name, Age, Gender, Doctor, Appointment
        self.table.setColumnCount(5)

        # Column headers (titles)
        self.table.setHorizontalHeaderLabels(
            ["Name", "Age", "Gender", "Doctor", "Appointment"]
        )

        # DISABLE EDITING IN TABLE
        # → users cannot change data manually inside table
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        layout.addWidget(self.table)

        # Set layout to window
        self.setLayout(layout)

    # FUNCTION: ADD BUTTON LOGIC
    def add(self):
        
        #This function runs when the ADD button is clicked.
        #It takes text from input fields and stores it in self.data.

        # Get values from all input fields
        row = [i.text() for i in self.inputs]

        # If name is empty → do nothing
        if row[0] == "":
            return

        # Add patient to data list
        self.data.append(row)

        # Clear all input boxes after adding
        for i in self.inputs:
            i.clear()

        # Update table display
        self.refresh()

    # FUNCTION: DELETE BUTTON LOGIC
    def delete(self):
        
        #This function runs when DELETE button is clicked.
        #It removes the selected row from the table.

        # Get selected row index in table
        r = self.table.currentRow()

        # If nothing is selected → do nothing
        if r >= 0:
            # Remove from data list
            self.data.pop(r)

            # Update table display
            self.refresh()

    # FUNCTION: UPDATE TABLE DISPLAY
    def refresh(self):
        """
        This function updates the table every time data changes.
        """

        # Set number of rows = number of patients
        self.table.setRowCount(len(self.data))

        # Fill table with data
        for i, row in enumerate(self.data):
            for j, val in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(val))


# RUN APPLICATION
app = QApplication(sys.argv)  # start app system
window = App()                 # create window object
window.show()                  # display window
sys.exit(app.exec())          # run event loop (keep app running)
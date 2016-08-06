# idoor-edison

Source code of an academic project using intel edison. Includes the code of the python script running in the intel edison and the code of the external web page. 

## About

Created to be an intermediary between the students and the school. 
Designed to be placed in every class with an auxiliary keypad in order to navigate through the different menus, 
which offered features like marks of exams or last assignments.
The identification of the students was made with a NFC lector and the personal university card.

## Structure

/Xlib & /nfc & /npyscreen & /pykeyboard & /pymouse  -- Dependencies  
/web -- All the source code from the web.   
/NFC.py -- Script used for reading the university card through the NFC reader.   
/buttons.py -- Script that read the GPIO Pins of the intel edison board.  
/controller.py -- Main script.   
/menu.py -- Represents the GUI and the data.  
/parser.py -- Parse the json from the web and helps creation of structured data.  
/script.py -- Auxiliary methods.

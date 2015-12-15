#!/usr/bin/env python
# encoding: utf-8

#TODO 

import npyscreen, random, script, time
#npyscreen.disableColor()
class TestApp(npyscreen.NPSAppManaged):
    def __init__(self, parser, controller):
    	self.parser = parser
    	parser.groupCreation()
    	self.controller = controller
    	self.run()
    def onStart(self):
        self.keypress_timeout = 400
        self.STARTING_FORM = 'zeroScreen'
        self.addForm('zeroScreen',zeroScreen)
        self.addForm('mainScreen',mainScreen)
        self.addForm('gradesScreen',gradesScreen)
        self.addForm('scheduleScreen',scheduleScreen)
        self.addForm('assignmentsScreen',assignmentsScreen)
        self.addForm('friendScreen',friendScreen)
        self.addForm('friendSuccesScreen',friendSuccesScreen)
        self.addForm('friendErrorScreen',friendErrorScreen)
    def h_exit_escape(self):
	    self.on_ok
    def while_waiting(self):
    	self.on_ok(self)
    # Metodo que se llama al seleccionar OK
    def on_ok(self):
    	self.controller.stop()
        
class zeroScreen(npyscreen.Form):
        def create(self):
             self.name = "IDOOR"
             self.lines=30
             self.columns=40
             self.pages_label_color='LABEL'
             self.add(CustomFixedText, name = "Siguiente Clase: ", value = "Siguiente Clase: " + self.parentApp.parser.nextClass())
             self.add(CustomFixedText, name = "Ultima nota: ", value = "Ultima nota: " + self.parentApp.parser.lastGrade())
             self.add(CustomFixedText, name = "Ultima tarea: ", value = "Ultima tarea: " + self.parentApp.parser.lastAssignment())
             self.add(mainButton, name = "Ir al menu principal")
             self.add(CSButton, name = "Cerrar session")
class mainScreen(npyscreen.Form):
        def create(self):
            self.name = "IDOOR"
            self.lines=30
            self.columns=40
            self.pages_label_color='LABEL'
	    fn = self.add(NotasButton, name = "Notas")
	    av = self.add(AvisosButton, name = "Avisos")
            dt = self.add(HorarioButton, name = "Horario")
            fb = self.add(FriendButton, name = "Añadir amigo")
	    lo = self.add(CSButton, name = "Cerrar session")
class gradesScreen(npyscreen.Form):
        def create(self):
            self.name = "IDOOR"
            self.lines=30
            self.columns=40
            self.pages_label_color='LABEL'
            t = self.add(CustomTitleText, name = "Notes:",)
            for x in range(parser.numGrades()):
                self.add_widget_intelligent(CustomFixedText, value = self.parentApp.parser.grades[x][0] + ' ' + self.parentApp.parser.grades[x][1] + ' ' + self.parentApp.parser.grades[x][2] )
            self.add(BackButton, name = "Volver al menu principal")
class scheduleScreen(npyscreen.Form):
        def create(self):
    	    self.name = "IDOOR"
            self.lines=30
            self.columns=40
            self.pages_label_color='LABEL'
    	    self.parentApp.parser.gridScheduleCreation(F.add(MyGrid, columns = 6, scroll_exit=True, exit_left = True,col_titles=['','Lunes','Martes','Miercoles','Jueves','Viernes']))
            self.add(BackButton, name = "Volver al menu principal")
class assignmentsScreen(npyscreen.Form):
        def create(self):
	    self.name = "IDOOR"
            self.lines=30
            self.columns=40
            self.pages_label_color='LABEL'
	    for x in range(parser.numAssignment()):
		      self.add_widget_intelligent(CustomFixedText, value = self.parentApp.parser.assignments[x][0]+':'+ self.parentApp.parser.assignments[x][1] +' para ' + self.parentApp.parser.assignments[x][2])
            self.add(BackButton, name = "Volver al menu principal")
class friendErrorScreen(npyscreen.Form):
        def create(self):
            self.name = "IDOOR"
            self.lines=30
            self.columns=40
            self.pages_label_color='LABEL'
            self.add(CustomFixedText, value = "La tarjeta que acercaste era la tuya. Por favor, acerca la de tu amigo")
            time.sleep(5)
            self.parentApp.switchForm('friendScreen')
class friendSuccesScreen(npyscreen.Form):
        def create(self):
            self.name = "IDOOR"
            self.lines=30
            self.columns=40
            self.pages_label_color='LABEL'
            self.add(CustomFixedText, value = "Perfecto! Ahora ya soy amigos")
            self.add(BackButton, name = "Volver al menu principal")
class friendScreen(npyscreen.Form):
        def create(self):
            self.name = "IDOOR"
            self.lines=30
            self.columns=40
            self.pages_label_color='LABEL'
            self.add(CustomTitleText, name = "Añadir amigo")
            self.add(CustomFixedText, value = "Acerque la tarjeta de su amigo")
            self.add(BackButton, name = "Volver al menu principal")
            time.sleep(3)
            check = script.friendAdd(parser.id)
            if check is 0:
                 self.parentApp.switchForm('friendSuccesScreen')
            else:
        	 self.parentApp.switchForm('friendErrorScreen')
      
class CustomFixedText(npyscreen.FixedText):
    how_exited = True

class CustomTitleSelectOne(npyscreen.TitleSelectOne):
    how_exited = True

class CustomTitleText(npyscreen.TitleText):
    how_exited = True

# Wrap para el widget Grid
class MyGrid(npyscreen.GridColTitles):
    select_whole_line = True
    how_exited = True
    scroll_exit = True
    # Modificacion de los colores con los que se hace display el grid
    def custom_print_cell(self, actual_cell, cell_display_value):
    	if cell_display_value < 5 or cell_display_value is '---':
      		actual_cell.color = 'DANGER'
    	elif cell_display_value >= 5:
       		actual_cell.color = 'GOOD'
       	else:
      		actual_cell.color = 'DEFAULT'
class BackButton(npyscreen.ButtonPress):
    	def whenPressed(self):
        	self.parentApp.switchForm('mainScreen')
        
class AvisosButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parentApp.switchForm('assignmentsScreen')

class CSButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.on_ok()
		
class NotasButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parentApp.switchForm('gradesScreen')

class HorarioButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parentApp.switchForm('scheduleScreen')

class mainButton(npyscreen.ButtonPress):
    	def whenPressed(self):
        	self.parentApp.switchForm('mainScreen')

class FriendButton(npyscreen.ButtonPress):
    	def whenPressed(self):
        	self.parentApp.switchForm('friendScreen')
        
if __name__ == "__main__":
    App = TestApp()
    App.run()

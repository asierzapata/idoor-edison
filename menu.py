#!/usr/bin/env python
# encoding: utf-8

#TODO 

import npyscreen, random, script, time
#npyscreen.disableColor()
class TestApp(npyscreen.NPSApp):
    def __init__(self, parser, controller):
	    self.parser = parser
	    parser.groupCreation()
	    self.controller = controller
        self.keypress_timeout = 400
        self.addFormClass('zeroScreen',zeroScreen)
        self.addFormClass('mainScreen',mainScreen)
        self.addFormClass('gradesScreen',gradesScreen)
        self.addFormClass('scheduleScreen',scheduleScreen)
        self.addFormClass('assignmentsScreen',assignmentsScreen)
        self.addFormClass('friendScreen',friendScreen)
        self.addFormClass('friendSuccesScreen',friendSuccesScreen)
        self.addFormClass('friendErrorScreen',friendErrorScreen)
        self.STARTING_FORM = 'zeroScreen'
    def h_exit_escape(self):
	    self.on_ok
    def while_waiting(self):
    	self.on_ok(self)
    # Metodo que se llama al seleccionar OK
    def on_ok(self):
    	self.controller.stop()
    '''def main(self):
    	#Definimos el timeout como 4 segundos
        self.switchForm('zeroScreen')'''
    def zeroScreen(npyscreen.FormMultiPageActionWithMenus):
        def create(self):
             F = npyscreen.FormMultiPageActionWithMenus(name = "IDOOR",lines=30,columns=40,pages_label_color='LABEL')
             F.add(CustomFixedText, name = "Siguiente Clase: ", value = "Siguiente Clase: " + parser.nextClass())
             F.add(CustomFixedText, name = "Ultima nota: ", value = "Ultima nota: " + parser.lastGrade())
             F.add(CustomFixedText, name = "Ultima tarea: ", value = "Ultima tarea: " + parser.lastAssignment())
             F.add(mainButton, name = "Ir al menu principal")
             F.add(CSButton, name = "Cerrar session")
             F.edit()   
    def mainScreen(npyscreen.FormMultiPageActionWithMenus):
        def create(self):
            F = npyscreen.FormMultiPageActionWithMenus(name = "IDOOR",lines=30,columns=40,pages_label_color='LABEL')
	    fn = F.add(NotasButton, name = "Notas")
	    av = F.add(AvisosButton, name = "Avisos")
            dt = F.add(HorarioButton, name = "Horario")
            fb = F.add(FriendButton, name = "Añadir amigo")
	    lo = F.add(CSButton, name = "Cerrar session")
            F.edit() 
    def gradesScreen(npyscreen.FormMultiPageActionWithMenus):
        def create(self):
            F = npyscreen.FormMultiPageActionWithMenus(name = "IDOOR",lines=30,columns=40,pages_label_color='LABEL')
            t = F.add(CustomTitleText, name = "Notes:",)
            for x in range(parser.numGrades()):
                F.add_widget_intelligent(CustomFixedText, value = self.parser.grades[x][0] + ' ' + self.parser.grades[x][1] + ' ' + self.parser.grades[x][2] )
            F.add(BackButton, name = "Volver al menu principal")
            F.edit()   
    def scheduleScreen(npyscreen.FormMultiPageActionWithMenus):
        def create(self):
    	    F = npyscreen.FormMultiPageActionWithMenus(name = "IDOOR",lines=30,columns=40,pages_label_color='LABEL')
    	    parser.gridScheduleCreation(F.add(MyGrid, columns = 6, scroll_exit=True, exit_left = True,col_titles=['','Lunes','Martes','Miercoles','Jueves','Viernes']))
            F.add(BackButton, name = "Volver al menu principal")
            F.edit()         
    def assignmentsScreen(npyscreen.FormMultiPageActionWithMenus):
        def create(self):
	    F = npyscreen.FormMultiPageActionWithMenus(name = "IDOOR",lines=30,columns=40,pages_label_color='LABEL')
	    for x in range(parser.numAssignment()):
		      F.add_widget_intelligent(CustomFixedText, value = parser.assignments[x][0]+':'+ parser.assignments[x][1] +' para ' + parser.assignments[x][2])
            F.add(BackButton, name = "Volver al menu principal")
            F.edit()
    def friendErrorScreen(npyscreen.FormMultiPageActionWithMenus):
        def create(self):
            F = npyscreen.FormMultiPageActionWithMenus(name = "IDOOR",lines=30,columns=40,pages_label_color='LABEL')
            F.add(CustomFixedText, value = "La tarjeta que acercaste era la tuya. Por favor, acerca la de tu amigo")
            time.sleep(4)
            F.switch_page(5)
            F.edit()
    def friendSuccesScreen(npyscreen.FormMultiPageActionWithMenus):
        def create(self):
            F = npyscreen.FormMultiPageActionWithMenus(name = "IDOOR",lines=30,columns=40,pages_label_color='LABEL')
            F.add(CustomFixedText, value = "Perfecto! Ahora ya soy amigos")
            F.add(BackButton, name = "Volver al menu principal")
            F.edit()
    def friendScreen(npyscreen.FormMultiPageActionWithMenus):
        def create(self):
            F = npyscreen.FormMultiPageActionWithMenus(name = "IDOOR",lines=30,columns=40,pages_label_color='LABEL')
            F.add(CustomTitleText, name = "Añadir amigo")
            F.add(CustomFixedText, value = "Acerque la tarjeta de su amigo")
            time.sleep(2)
            check = script.friendAdd(parser.id)
            if check is 0:
                F.switch_page(5)
            else:
        	F.switch_page(6)
            F.add(BackButton, name = "Volver al menu principal")
            F.edit()
      
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

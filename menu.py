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
	self.keypress_timeout = 40
    def h_exit_escape(self):
	self.on_ok
    def while_waiting(self):
    	self.on_ok(self)
    # Metodo que se llama al seleccionar OK
    def stop(self):
    	self.controller.stop()
    def on_ok(self):
    	self.controller.stop()
    def main(self):
	# Creacion del Form y de los botones de la 1a pagina
        F = npyscreen.FormMultiPageActionWithMenus(name = "IDOOR",lines=30,columns=40,pages_label_color='LABEL')
        F.edit_return_value = 1
        parser = self.parser
	#F.how_exited_handers[npyscreen.widget.EXITED_ESCAPE]  = self.exit_application
        F.add(CustomFixedText, name = "Siguiente Clase: ", value = "Siguiente Clase: " + parser.nextClass())
        F.add(CustomFixedText, name = "Ultima nota: ", value = "Ultima nota: " + parser.lastGrade())
        F.add(CustomFixedText, name = "Ultima tarea: ", value = "Ultima tarea: " + parser.lastAssignment())
        F.add(CustomFixedText, name = "Ultima posicion de algun amigo: ", value = "Ultimo posicion de algun amigo: ")
        F.add(CustomFixedText, name = "amigo", value = "  " + parser.lastCheck())
        F.add_widget_intelligent(CSButton, name = "Cerrar session")
        #Creacion de la pagina 1
	P1 = F.add_page()
	fn = F.add(NotasButton, name = "Notas")
	av = F.add(AvisosButton, name = "Avisos")
        dt = F.add(HorarioButton, name = "Horario")
        fr = F.add(FriendListButton, name = "Lista de amigos")
        fb = F.add(FriendButton, name = "Anadir amigo")
	lo = F.add(CSButton, name = "Cerrar session")        
        # Creacion pagina 2
        P2 = F.add_page()
        t = F.add(CustomTitleText, name = "Notes:",)
        # TODO Cambiar formato del display de las notas a grid
        for x in range(parser.numGrades()):
                F.add_widget_intelligent(CustomFixedText, value = parser.grades[x][0] + ' ' + parser.grades[x][1] + ' ' + parser.grades[x][2] )
        F.add_widget_intelligent(BackButton, name = "Volver al menu principal")
        # Creacion pagina 3
    	P3 = F.add_page()
    	parser.gridScheduleCreation(F.add(MyGrid, columns = 6, scroll_exit=True, exit_left = True,col_titles=['','Lunes','Martes','Miercoles','Jueves','Viernes']))
        #F.add(BackButton, name = "Volver al menu principal")
	# Creacion pagina 4
	P4 = F.add_page()
	for x in range(parser.numAssignment()):
		F.add_widget_intelligent(CustomFixedText, value = parser.assignments[x][0]+':'+ parser.assignments[x][1] +' para ' + parser.assignments[x][2])
        F.add_widget_intelligent(BackButton, name = "Volver al menu principal")
        # Creacion pagina 5
        P6 = F.add_page()
        F.add(CustomFixedText, value = "La tarjeta que acercaste era la tuya.")
        F.add(CustomFixedText, value = "Por favor, acerca la de tu amigo.")
        rb1 = F.add(ReadyButton, name= "Continuar")
        rb1.setParser(self.parser)
        F.add(BackButton, name = "Volver al menu principal")
        # Creacion pagina 6
        P6 = F.add_page()
        F.add(CustomFixedText, value = "Perfecto! Ahora ya soy amigos")
        F.add(BackButton, name = "Volver al menu principal")
        # Creacion pagina 7
        P7 = F.add_page()
        F.add(CustomTitleText, name = "Añadir amigo")
        F.add(CustomFixedText, value = "Acerque la tarjeta de su amigo.")
        F.add(CustomFixedText, value = "Cuando estes preparado selecciona Continuar.")
        rb2 = F.add(ReadyButton, name= "Continuar")
        rb2.setParser(self.parser)
        F.add(BackButton, name = "Volver al menu principal")
        # Creacion pagina 8
        P8 = F.add_page()
        for x in range(parser.numFriends()):
		F.add_widget_intelligent(CustomFixedText, value = parser.friends[x]['nombre']+' en '+ parser.friends[x]['last_place_check'] + ' ')
		F.add_widget_intelligent(CustomFixedText, value = parser.friends[x]['last_check'])
		F.add_widget_intelligent(CustomFixedText, value = " ")
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
    		self.parent.DISPLAY()
        	self.parent.switch_page(1)
        
class AvisosButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.DISPLAY()
		self.parent.switch_page(4)

class CSButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.editing = False
		self.parent.on_ok()

class ReadyButton(npyscreen.ButtonPress):
	def setParser(self,parser):
		self.parser = parser
	def whenPressed(self):
		check = script.friendAdd(self.parser.id)
		if check is 0:
			self.parent.DISPLAY()
            		self.parent.switch_page(5)
        	else:
        		self.parent.DISPLAY()
        		self.parent.switch_page(6)
class NotasButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.DISPLAY()
		self.parent.switch_page(2)

class HorarioButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.DISPLAY()
		self.parent.switch_page(3)

class FriendListButton(npyscreen.ButtonPress):
	def whenPressed(self):
		self.parent.DISPLAY()
		self.parent.switch_page(8)

class FriendButton(npyscreen.ButtonPress):
    	def whenPressed(self):
    		self.parent.DISPLAY()
        	self.parent.switch_page(7)
        
if __name__ == "__main__":
    App = TestApp()
    App.run()

#!/usr/bin/env python

import re, time, script, urllib2

class parser:
	def __init__(self, response):
		self.datos = response[0].read()
		self.id = response[1]
		self.groupCreation()
		self.day = time.strftime("%A")
		self.traduction()
		self.nextHour = str(int(time.strftime("%H"))+1)
		self.nextclass = "None"
		self.assignments = []
		self.date = time.strftime("%Y")+"-"+time.strftime("%m")+"-"+time.strftime("%d")
	def traduction(self):
		if self.day == 'Monday': self.day = 'Lunes'
		if self.day == 'Tuesday': self.day = 'Martes'
		if self.day == 'Wednesday': self.day = 'Miercoles'
		if self.day == 'Thursday': self.day = 'Jueves'		
		if self.day == 'Friday': self.day = 'Viernes'
	def nextClass(self):
		r = script.findNextClass(self.horario)
		return r
	def lastGrade(self):
		tmp = self.grades[len(self.grades)-1]
		r = tmp[0] +' '+ tmp[1]+' '+ tmp[2]
		return r
	def numGrades(self):
		return len(self.grades)
	def lastAssignment(self):
		near = script.nearAssignment(self.assignments)
		return near
	def numAssignment(self):
		return len(self.assignments)
	def gridScheduleCreation(self,gd):
		gd.values = []
        	horas = ['8','9','10','11','12','13','14','15','16','17','18','19','20']
        	dias = ['Lunes','Martes','Miercoles','Jueves','Viernes']
		'''aux = []
	        hcount = 0
		for w in range(len(horas)):
			m = re.search(horas[w], self.horario)
			if m != None:
	     			hcount += 1
                 
        	aux = self.horario.split('},"',hcount)
        	aux[hcount-1] = aux[hcount-1][:len(aux[hcount-1])-1]
        	for q in range(len(aux)):
            		aux[q] = re.split(",",aux[q])
            		m = re.match(r"(.*?)\":\{(\"(.*?)\":\"(.*?)\")",aux[q][0])
	        	aux[q][0] = m.group(2)
       	    		aux[q].append(m.group(1))
        	for x in horas:
            		for y in range(len(aux)):
                		t = re.search(x,aux[y][len(aux[y])-1])
                		if t != None:
                    			row = []
                    			row.append(x)
                    			for z in dias:
                        			for d in range(len(aux[y])-1):
                            				dayPattern = re.compile(r"\"(.*?)\":\"(.*?)\"")
							t = dayPattern.match(aux[y][d])
							if t.group(1) == z:
								if self.day == z and self.nextHour == x: 
									self.nextclass = t.group(2)
									row.append(t.group(2))
									break
								if d == len(aux[y])-2:
									row.append("---")  
                    			gd.values.append(row)
		if self.nextclass == None: 
			self.nextclass = "Proximo dia"
        '''
        	for x in horas:
        		row = []
        		for y in dias:
                		try:
                	        	row.append(self.horario[x][y])
        			except KeyError:
                	        	row.append("---")
        		gd.values.append(row)

	def groupCreation(self):
		tareas = re.compile("tareas")
		horario = re.compile("horario")
		notas = re.compile("NOTAS")
		x = tareas.search(self.datos)
		y = horario.search(self.datos)
		z = notas.search(self.datos)
		self.tareas = self.datos[x.start()+9:y.start()-4]
		self.horario = urllib2.urlopen('http://raiblax.com/pbe/receptor.php?id_alumno='+self.id+'&modo').read()
		self.notas = self.datos[z.start()+6:len(self.datos)-1]
		#Creacion del array de tareas
		pattern = re.compile(r"\"siglas_asignatura\":\"(.*?)\",\"tarea\":\"(.*?)\",\"entrega\":\"(.*?)\"")
        	self.assignments = pattern.findall(self.tareas)
		#Creacion del array de notas
		pattern = re.compile(r"(.*?):(.*?):(.*?)/")
        	self.grades = pattern.findall(self.notas)

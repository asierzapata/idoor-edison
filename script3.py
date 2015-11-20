import script, urllib2, re

response = urllib2.urlopen('http://raiblax.com/pbe/receptor.php?id_alumno=FB68CCF1')
datos = response.read()
print datos
print "---------------------------"
tareas = re.compile("tareas")
horario = re.compile("horario")
notas = re.compile("NOTAS")
x = tareas.search(datos)
y = horario.search(datos)
z = notas.search(datos)
tareas = datos[x.start()+9:y.start()-4]
horario = datos[y.start()+11:z.start()-2]
notas = datos[z.start()+6:len(datos)-1]
pattern = re.compile(r"\"siglas_asignatura\":\"(.*?)\",\"tarea\":\"(.*?)\",\"entrega\":\"(.*?)\"")
assignments = pattern.findall(tareas)
pattern2 = re.compile(r"(.*?):(.*?):(.*?)/")
grades = pattern2.findall(notas)
print "assignments: "
print assignments
print "---------------------------"
print "grades: "
print grades
print "---------------------------"
print "horario: "
print horario
print "---------------------------"
print "Proxima tarea: "
print script.nearAssignment(assignments)

import re, time, NFC

def nearAssignment(assignments):
        near = ''
	r = ''
        for x in range(len(assignments)):
                tmp = assignments[x][2]
                if near == '':
                        near = tmp
			r = assignments[x][0]+' '+assignments[x][2]
                elif near[0:4] == tmp[0:4]:
                        if near[5:7] == tmp[5:7]:
                                if near[8:10] > tmp[8:10]:
                			r = assignments[x][0]+' '+assignments[x][2]  
		                        near = tmp
        return r

def findNextClass(H,day):
	nextHour = str(int(time.strftime("%H"))+1)
	dias = ['Lunes','Martes','Miercoles','Jueves','Viernes']
	horas = ['8','9','10','11','12','13','14','15','16','17','18','19','20']
	r = None
	for x in horas:
        	if x == nextHour:
                	try:
                	        r = H[nextHour][day]
        		except KeyError:
                        	nextHour = str(int(nextHour)+1)
	if r == None:
        	r = "Proximo dia"
	return r

def friendAdd(my_id):
        nfc = NFC.NFC()
        while True:
                response = nfc.read('http://raiblax.com/pbe/receptor.php?id_alumno=')
                if response != None:
                        break
        friend_id = response[1]
        # Control errors: les dues id son iguals
        if friend_id == my_id:
                return 0
        # Enviar la id del amic al servidor
        else:
                urllib2.urlopen('http://raiblax.com/pbe/receptor.php?id_alumno=' + my_id + '&friend' + friend_id)

import re, time

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
                                        #if tmp[8:10] >= time.strftime("%d"):
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

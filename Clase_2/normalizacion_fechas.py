##fecha = "13/2/2019"
##fecha = "2/13/2019"
##fecha = "02/19" (mes/año)
##fecha = "20191302"
##fecha = "2019-13-02 14:23:33"
##fecha = "13/Feb/2019"
##fecha = "13/February/2019"
##fecha = "13 days after February 2019"
##fecha = "13/Febrero/2019"

#fecha_output="13-02-2019"

from datetime import datetime

def normalizadorFechas(fecha, patron_in, patron_out = '%d-%m-%Y'):
    objeto_fecha = datetime.strptime(fecha, patron_in)
    fecha_normalizada = datetime.strftime(objeto_fecha, patron_out)
    print(fecha, '->', objeto_fecha, '->', fecha_normalizada)
    
fecha = "13/2/2019"    
normalizadorFechas(fecha, %d/%m/%Y)
    
fecha = '20191302'
normalizadorFechas(fecha, '%Y%d%m')

fecha = "2/13/2019"
normalizadorFechas(fecha, '%m/%d/%Y')
from app.wsgi import *
from core.erp.models import Type, Empleado

# Listar

# SELECT * FROM Tabla

# query = Type.objects.all()
# print(query)

# Insetar datos
# Type(nombre="Contable").save()

#Actualizar
# tipo = Type.objects.get(id = 3)
# tipo.nombre = "Contable"
# tipo.save()

# Eliminar
# con = Type.objects.filter(id=4)
# con.delete()

#Listar filter

# r = Type.objects.filter(nombre__icontains='ta')
# r = Type.objects.filter(nombre__istartswith='co').query
# print(r)

print(Empleado.objects.filter(type_id=1))

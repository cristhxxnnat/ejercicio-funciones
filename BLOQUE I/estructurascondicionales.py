sistemaActivo: bool = True
tienePermiso: bool = False

if sistemaActivo == True:
    if tienePermiso == True:
        print("Acción ejecutada")
    else:
        print("Permiso denegado")
else: 
    print("Sistema inactivo")

    


    
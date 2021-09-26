import send2trash, os, shutil

# el modulo walk permite ver el path de los elementos que pertenezcan a
# una carpeta indicada entre ()
# este modulo permite hacer un muestreo de todos los archivos y carpetas
# que esten contenidas en det path

for Car_N, SubCarps, files_N in os.walk(os.getcwd()):
    print ('Carpeta actual es '+ Car_N)

    for SubCar in SubCarps:
        print('\nSub Carpeta de '+ Car_N +': '+ SubCar)

        for files in files_N:
            print ('Archivos de la carpeta:' + SubCar+': '+files)            

# este metodo devuelve como resultado una list de los nombres de las 
# carpetas y archivos contenidos en cierto directorio
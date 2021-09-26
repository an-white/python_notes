import send2trash

# El modulo send2trash permite enviar a la papelera los archivos deseados
# No se por que este si me lo permite ejecutar win

txt=open('info.txt','w')
txt.write('comida comer cerebroooo :v')
txt.close()
input()
send2trash.send2trash('info.txt')

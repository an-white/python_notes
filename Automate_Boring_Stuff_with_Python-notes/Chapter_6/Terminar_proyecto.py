# pw.py - Una clave insegura
claves = {'email': 'a1a2a3a4a5a6a7a8a9a0',
          'Blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
          'Banco': 'Morro123'}
import pyperclip
import sys

if len(sys.argv) < 2:
    print('Usage: python pw.py [Cuenta]- copiar clave de cuenta')
    sys.exit()

cuenta = sys.argv[1]
if cuenta in claves:
    pyperclip.copy(clave[cuenta])
else:
    print('No hay un usuario para esa cuenta' + cuenta)

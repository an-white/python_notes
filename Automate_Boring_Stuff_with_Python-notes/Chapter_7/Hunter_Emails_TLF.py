# añadir errores comunes en los @gmail,@hotmail,@yahoo,@outlook
import pyperclip
import re

ID_TLFs = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # Codigo de area Opcional puede estar entre ()
    (\s|-|\.)?                          # Tipo de separador
    \d{3}                               # primeros 3 digitos
    (\s|-|\.)                           # Tipo de separador
    \d{4}
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

# Def de Emails
ID_Emails = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
(|gmail|hotmail|yahoo|outlook)#[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE | re.I | re.DOTALL)

txt = str(pyperclip.paste())
Encontrados = []

for groups in ID_TLFs.findall(txt):
    TLFs = '-'.join(groups[1], groups[3], groups[5])
    if groups[8] != '':
        TLFs += ' x' + groups[8]
    Encontrados.append(groups[0])
for groups in ID_Emails.findall(txt):
    Encontrados.append(groups[0])

if len(Encontrados) > 0:
    pyperclip.copy('\n'.join(Encontrados))
    print('Copiados:')
    print('\n'.join(Encontrados))
else:
    print('No se ha conseguido ningun Numero telefonico ni email que cumpla con las estructuras establecidas.')

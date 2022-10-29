import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=30))


# el decorador dataclass puede agregarsele el parametro frozen con la cual cada instancia
# del objeto en inmutable

# el parametro kw_only permite setear si es obligatorio definir o no el nombrer de las kw que se van
# a establecer en la instancia del objeto
@dataclass(frozen=False, kw_only=True)
class Box:
    # id auto generado que no puede ser seteado al instanciar el valor
    box_id: str = field(init=False, default_factory=generate_id)
    name: str
    address: str
    # valor por defecto asignado
    fragile: bool = False
    # generar una lista independiente por cada instancia de la clase
    email_addresses: list[str] = field(default_factory=list)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self):
        self._search_string = f"{self.name}, ID:{self.box_id}"


if __name__ == '__main__':
    new_box = Box(name='my box c:', address='my house')
    sec_box = Box(name='my 2nd box c:', address='my house2', email_addresses=['myemail@test.com', 'mail@haus.com'])
    print(new_box, '\n', sec_box)

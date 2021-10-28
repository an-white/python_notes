import re
data=r"""
Archaeologist: Arqueólogo.
Architect: Arquitecto.
Astronaut: Astronauta.
Baker: Panadero.
Biologist: Biólogo/a.
Bricklayer: Albañil.
Bus driver: Conductor/a de autobús.
Businessman: Empresario, hombre de negocios.
Businesswoman: Empresaria, mujer de negocios.
Butcher: Carnicero/a.
Caretaker: Portero, conserje.
Carpenter: Carpintero/a.
Cashier: Cajero/a.
Cleaner: Limpiador, mujer de la limpieza.
Clown: Payaso.
Cobbler: Zapatero.
Consultant: Consultor.
Cook: Cocinero.
Counselor: Asesor, consultor.
Chef: Cocinero (profesional).
Chemist: Químico, farmaceútico.
Dancer: Bailarín.
Decorator: Decorador.
Dentist: Dentista.
Designer: Diseñador.
Doctor: Médico/a.
Dressmaker: Modista.
Dustman: Basurero (UK).
Economist: Economista.
Electrician: Electricista.
Engineer: Ingeniero/a.
Farmer: Granjero, agricultor.
Fireman: Bombero.
FIsherman: Pescador.
Florist: Florista.
Fruiterer: Frutero.
Garbage collector: Basurero (USA).
Gardener: Jardinero/a.
Hairdresser: Peluquero/a.
Housewife: Ama de casa.
Hunter: Cazador.
Jeweller: Joyero/a.
Journalist: Periodista.
Judge: Juez.
Lawyer: Abogado/a.
Librarian: Bibliotecario/a.
Life guard: Socorrista.
Lorry driver: Camionero/a (UK).
Mailman: Cartero (USA).
Mechanic: Mecánico/a.
Meteorologist: Meteorólogo.
Miner: Minero/a.
Model: Modelo.
Monk: Monje.
Nanny: Niñera.
Nun: Monja.
Nurse: Enfermero/a.
Nursemaid: Niñera.
Office worker: Oficinista.
Painter: Pintor.
Pastry cook: Pastelero, repostero.
Pharmacist: Farmaceútico.
Photographer: Fotógrafo.
Physicist: Físico.
Plumber: Fontanero.
Policeman / Policewoman: Policía.
Politician: Político.
Porter: Conserje.
Postman: Cartero (UK).
Priest: Cura.
Professor: Profesor/a (Universidad).
Programmer: Programador.
Psychiatrist: Psiquiatra.
Psychologist: Psicólogo/a.
Receptionist: Recepcionista.
Researcher: Investigador.
Sailor: Marinero/a.
Salesman: Vendedor.
Scientist: Científico.
Secretary: Secretario.
Shoemaker: Zapatero.
Shop assistant: Dependiente/a de una tienda.
Singer: Cantante.
Social worker: Trabajador social.
Sportsman: deportista.
Surgeon: Cirujano.
Taxi driver: Taxista.
Teacher: Profesor/a (Primaria y Secundaria).
Telephone operator: Telefonista.
Travel agent: Agente de viajes.
Truck driver: Camionero/a (USA).
Vet: Veterinario (UK).
Veterinarian: Veterinario (USA).
Waiter: Camarero/a (bar).
Waitress: Camarera, mesera.
Window cleaner: Limpiacristales.
"""
filter=re.compile(r"\n(.+):")
pro= filter.findall(data)
professions='\n'.join(pro)
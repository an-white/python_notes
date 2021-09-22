container = {
    "a":"alfa",
    "b":"beta",
}
# otra forma de acceder a una key de un diccionario con la funcion get
print(container.get("a"))
kwargs={
    "page": 1,
    "pagination": 25,
}

container = {
            "_metadata":{
                "page": kwargs["page"],
                "per_page": kwargs["pagination"],
                "page_count": 20,
                "total_count": 521,
                },
            "records":[
                {
                "author": "Juan",
                "content": "comment1",
                "property": "Valencia",
                "date": "16/07/2021",
                },
                {
                "author": "Admin_01",
                "content": "comentario superior a cuaranta caracteres",
                "property": "Sevilla",
                "date": "15/07/2021",
                },
                {
                "author": "Carmen",
                "content": "Comentario inferior a 40 caracteres",
                "property": "Valencia",
                "date": "20/01/2021",
                },
            ]    
        }

container["content"]="otra forma de acceder a una key de un diccionario con la funcion get"

for record in range(len(container["records"])):
    if len(container["records"][record]["content"]) > 40:
        container["records"][record]["preview"] = f"""{container["records"][record]["content"][0:40]}..."""
    else:
        container["records"][record]["preview"]  = container["records"][record]["content"]

print(container)
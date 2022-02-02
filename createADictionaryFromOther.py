from datetime import datetime

init = datetime.now()
for n in range(100000000):
    pass
end = datetime.now()
print(end - init)
container = {
    "_metadata": {
        "page": 1,
        "per_page": 25,
        "page_count": 20,
        "total_count": 521,
    },
    "records": [
        {
            "author": "Juan",
            "comment": "comment1",
            "property": "Valencia",
            "date": "16-07-2021",
        },
        {
            "author": "Admin_01",
            "comment": "comentario superior a cuaranta caracteres",
            "property": "Sevilla",
            "date": "15-07-2021",
        },
        {
            "author": "Carmen",
            "comment": "Comentario inferior a 40 caracteres",
            "property": "Valencia",
            "date": "20-01-2021",
        },
    ],
}
date_list = []
for record in range(len(container["records"])):
    # date format
    date = datetime.strptime(container["records"][record]["date"], "%d-%m-%Y")
    container["records"][record]["date"] = date.strftime("%d/%m/%Y")
    date_list.append(date.strptime(container["records"][record]["date"], "%d/%m/%Y"))

    # create preview
    if len(container["records"][record]["comment"]) > 40:
        container["records"][record][
            "preview"
        ] = f"""{container["records"][record]["comment"][0:40]}..."""
    else:
        container["records"][record]["preview"] = container["records"][record][
            "comment"
        ]

columns_list = ["author", "preview", "comment", "property", "date"]
result_list = []
for i in range(len(container["records"])):
    temp = {}
    for column in columns_list:
        temp[column] = container["records"][i][column]
    result_list.append(temp)

print(result_list)

import json

pedidos_1 = open('pedidos20230215.md', 'r')
pedidos_2 = open('pedidos20230216.md', 'r')

list_orden_15 = pedidos_1.readlines()
list_orden_16 = pedidos_2.readlines()

json_15 = {
    "Records": [

    ]
}
json_16 = {}

for line in list_orden_16:
    num_orden, id_customer = line.split(' ')
    record = {
        "body": """{
  \"Message\" : \"{\\\"CASA\\\":0,\\\"schema\\\":\\\"dbafv\\\",\\\"data\\\":{\\\"NUMORDEN\\\":\\\"""" +
                num_orden +
                """\\\",\\\"IDCLIENTE\\\":\\\"""" +
                id_customer[0:-1] + """\\\"}}\"}"""
    }
    json_15["Records"].append(record)

    new_file = open('sendPedido.json', 'w')

    new_file.write(json.dumps(json_15))

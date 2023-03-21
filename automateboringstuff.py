import json
import time


def build_json():
    # orders file must have the next structure
    """ orders.md
    NUMORDEN1 IDCLIENTE1
    NUMORDEN2 IDCLIENTE2
    """
    # this structure is the easy way to build all the orden JSONs

    orders_file = open('orders.md', 'r')

    list_orden = orders_file.readlines()

    new_json = {
        "Records": [

        ]
    }
    json_16 = {}

    for line in list_orden:
        num_orden, id_customer = line.split(' ')
        record = {
            "body": """{
      \"Message\" : \"{\\\"CASA\\\":0,\\\"schema\\\":\\\"dbafv\\\",\\\"data\\\":{\\\"NUMORDEN\\\":\\\"""" +
                    num_orden +
                    """\\\",\\\"IDCLIENTE\\\":\\\"""" +
                    id_customer[0:-1] + """\\\"}}\"}"""
        }
        new_json["Records"].append(record)

    new_file = open(f'sendPedido{int(time.time())}.json', 'w')

    new_file.write(json.dumps(new_json))


if __name__ == '__main__':
    build_json()

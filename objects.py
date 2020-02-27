# -*- coding: utf-8 -*-

# Object from my thesis....
def isField(k):
    fields = [  {'key': 'price', 'value': ['precio', 'precios'], },
                {'key': 'dimension', 'value': ['construido'], },
                {'key': 'bedroom',    'value': ['dormitorio', 'dormitorios'], },
                {'key': 'living_room',    'value': ['sala', 'sala de estar'], },
                {'key': 'dinning_room',    'value': ['comedor de diario'], },
                {'key': 'bath_room', 'value': ['baño', 'baños'], },
                {'key': 'garage',    'value': ['portón eléctrico', 'garaje', 'garajes'], },
                {'key': 'garden',    'value': ['jardín', ]},
                {'key': 'pool',    'value': ['piscina'], },
                {'key': 'neighborhood', 'value': ['zona'], },
                {'key': 'city', 'value': ['ciudad'], },
                {'key': 'floor', 'value': ['piso', 'pisos'], },
                {'key': 'status', 'value': ['estado'], },
                {'key': 'year_built', 'value': ['año construcción'], },
                {'key': 'electricity_service', 'value': ['electricidad'], },
                {'key': 'water_service', 'value': ['agua'], },
                {'key': 'gas_service', 'value': ['gas natural'], },
                {'key': 'type_offer', 'value': ['alquiler', 'venta', 'anticrético']}
             ]

    # Searching a field in an object
    for f in fields:
        for v in f['value']:
            if v == k.lower():
                return f['key']

    return 'error'

# Test cases..
fieldd = isField("construido")
field = isField("comedor dediario")
print("fiel->", fieldd)

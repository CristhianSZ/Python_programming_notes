"""precios_cafe = {
    "cafe_arabica": 5,
    "cafe_robusta": 4,
    "cafe_especial": 7
}

cafecaro = max(precios_cafe, key=precios_cafe.get)
precio_mas_caro = precios_cafe[cafecaro]

print("El café más caro es", cafecaro, "con un precio de", precio_mas_caro)"""



precios_cafe = {
    "cafe_arabica": 5,
    "cafe_robusta": 4,
    "cafe_especial": 7
}

cafecaro = ""
precio_mas_caro = 0

for cafe, precio in precios_cafe.items():
    if precio > precio_mas_caro:
        cafecaro = cafe
        precio_mas_caro = precio

print("El café más caro es", cafecaro, "con un precio de", precio_mas_caro)


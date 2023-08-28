"""listas=["anana","pera","pera"]
set={"anana","pera","manazana"}
#vectores van entre corchetes y ser con llaves"""
"""Verfica si los sets a continuacion forman conjuntos aislados (es decir, que no tienen elementos en comun),
utilizando el metodo isdishoint().Almacena dicha resultado en la variable conjuntos_aislados"""
marcas_celular={"LG","samsung","motorola","xiomi"}
marcas_tv={"samsung","philips","sony","LG"}
conjuntos_aislados = marcas_celular.isdisjoint(marcas_tv)
print(conjuntos_aislados)
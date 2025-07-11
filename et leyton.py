#Creo el diccionario de productos con sus claves y sus valores.
productos = {
'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
}

#Tambien creo el diccionario stock con sus claves y sus valores.
stock = {'8475HD': [387990,10],
         '2175HD': [327990,4],
         'JjfFHD': [424990,1],
         'fgdxFHD': [664990,21],
         '123FHD': [290890,32],
         '342FHD': [444990,7],
         'GF75HD': [749990,2],
         'UWU131HD': [349990,1],
         'FS1230HD': [249990,0],
}


#funcion para ver el stock de la marca:
def stock_marca(marca):
    total = 0
    for codigo, datos in productos.items():
        if datos[2].lower() == marca.lower():
            total += stock[codigo[1]]
    print(f"El stock de la marca {marca} es: {total}")


#funcion para la busqueda por precio:
def busqueda_precio(precio_minimo, precio_maximo):
    resultados = []
    for codigo, datos in productos.items():
        precio = datos[0]
        if precio >= precio_minimo and precio <= precio_maximo and stock[codigo][1] > 0:
            resultados.append(codigo + '--' + datos[0])

    if resultados:
        resultados.sort()
        print("Los notebooks entre los precios consultas son:", resultados)
    else:
        print("No hay productos con ese rango de precio.")


#funcion para ver el listado de productos:
def ordenar_productos():
    print("-------Listado de notebooks ordenados-------")
    print(productos)
    print("----------------------------------------------------")


#programa principal...
def main():
    while True:
        print("***MENU PRINCIPAL***")
        print("1. Stock marca.")
        print("2. Busqueda por precio.")
        print("3. Listado de productos")
        print("4. Salir.")
        opc = int(input("Ingrese una opcion del menu porfavor: "))

        if opc == 1:
            marca = input("Ingrese la marca a consultar:")
            stock_marca(marca)
        elif opc == 2:
            try:
                precio_min = float(input("Ingrese precio minimo: "))
                precio_max = float(input("Ingrese precio maximo: "))
                busqueda_precio(precio_min, precio_max)
            except ValueError:
                print("Debe ingresar valores enteros!!")

        elif opc == 3:
            ordenar_productos()

        elif opc == 4:
            print("Programa finalizado.")
            break
        else:
            print("Debe seleccionar una opcion valida!!")

#para ejecutar el programa
if __name__== "__main__":
    main()
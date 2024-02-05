def guardar_texto(texto, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(texto)
    print(f'Texto guardado en {nombre_archivo}')

def restaurar_texto(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            texto = archivo.read()
        print('Texto restaurado:')
        print(texto)
    except FileNotFoundError:
        print(f'El archivo {nombre_archivo} no existe. No se puede restaurar el texto.')

def main():
    nombre_archivo = 'texto_guardado.txt'

    # Guardar texto
    texto_usuario = input('Escribe tu texto: ')
    guardar_texto(texto_usuario, nombre_archivo)

    # Restaurar texto
    input('Presiona Enter para restaurar el texto...')
    restaurar_texto(nombre_archivo)

if __name__ == "__main__":
    main()
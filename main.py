import os
from managers.administrador_coleccion import AdministradorColeccion
admin = AdministradorColeccion()
admin.agregar_elemento
def mostrar_menu_principal():
    print("\n" + "="*50)
    print("   >ADMINISTRADOR DE COLECCIÓN<")
    print("-" * 50)
    print("1. Agregar un Elemento a la Colección")
    print("2. Listar Toda la Colección")
    print("3. Buscar un Elemento por Título")
    print("4. Filtrar un Elemento por su Género")
    print("5. Editar un Elemento Existente")
    print("6. Eliminar Elemento")
    print("7. Ver la Estadística de La Colección")
    print("8. Guardar cambios y salir")
    print("0. Salir del administrador sin guardar...")
    print("-" * 50)
    print("="*50)

def main():
    print("WELCOME TO Administrador de coleccion")
administrador_coleccion = AdministradorColeccion()

while (True):
    mostrar_menu_principal()
    
    try:
        opcion = input("Seleciona una opcion del 0 a 9: ").strip()
        
        if opcion == "1":
            administrador_coleccion.agregar_elemento() 
        elif opcion == "2":
            administrador_coleccion.listar_coleccion()
        elif opcion == "3":
            administrador_coleccion.buscar_elemento()
        elif opcion == "4":
            administrador_coleccion.filtrar_por_genero()
        elif opcion == "5":
            administrador_coleccion.editar_elemento()
        elif opcion == "6":
            administrador_coleccion.eliminar_elemento()
        elif opcion == "7":
            administrador_coleccion.mostrar_estadisticas()
        elif opcion == "8":
            if administrador_coleccion.guardar_datos():
                print("Datos gusrdados con exito:)")
                break
            else:
                print("Ocurrio un problema al guardar intente otra vez")
        elif opcion == "0":
            print("Hasta pronto")
            break
        else: 
            print("Opción inválida. Por favor, selecciona una opción del 0 al 8")
    
    except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
    except Exception as e:
        print(f" error: {e}")
        print("intentalo mas tarde")


if __name__ == "__main__":
    main()        
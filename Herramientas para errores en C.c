//HERRAMIENTAS PARA LOS ERRORES EN C

//PRIMERO (FUNCIÓN PARA VERIFICAR EL ERROR)
int miFuncion() {
    // Realizar operación
    if (ocurrioError) {  //se crea una función que verifique si hay errores en el sistema
        return -1; // Código de error
    }

    // Resto del código si la operación fue exitosa
    return 0; // Éxito
}

//SEGUNDO (HERRAMIENTA errno)
#include <errno.h>
#include <stdio.h>
#include <string.h>

int main() {
    FILE *archivo = fopen("archivo.txt", "r");
    if (archivo == NULL) {
        perror("Error al abrir el archivo");
        printf("Descripción del error: %s\n", strerror(errno)); //Nos apunta directamente el error de nuestra ejecución
        return 1;
    }

    // Resto del código si la operación fue exitosa

    fclose(archivo);
    return 0;
}

//TERCERO (HERRAMIENTA TRY-CATCH)
void f() {
    exception e;
    Try { //Se crea un codigo propenso a excepciones
        procesamiento_complejo();
        mas_procesamiento_complejo();
        todavia_mas_procesamiento_complejo();
    }
    Catch(e) {
        if (e.error_code != ERROR_NO_MAS_DATOS)
            Throw e;
    }
}

void g() {
    exception e;
    Try {
        f();
    Catch(e) {
        fprintf(stderr, "Error: %s\n", e.what);
    }
}
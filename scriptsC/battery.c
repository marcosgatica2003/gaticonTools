#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE* archivoCapacidad;
    FILE* archivoEstado;
    unsigned int capacidad = 0;
    char estado[32]= {0};

    archivoCapacidad = fopen("/sys/class/power_supply/BAT1/capacity", "r");
    archivoEstado = fopen("/sys/class/power_supply/BAT1/status", "r");

    if (archivoCapacidad == NULL || archivoEstado == NULL) {
        fprintf(stderr,"Error al acceder a la batería");
        fclose(archivoEstado); fclose(archivoCapacidad);
        return 1;
    }

    fscanf(archivoCapacidad, "%d", &capacidad);
    fscanf(archivoEstado, "%31s", estado);
    fclose(archivoCapacidad); fclose(archivoEstado);
    ( strcmp(estado, "Charging") == 0 ) ? printf("^c#222222^^b#d79921^  ⚡%d%% ^d^",capacidad) : printf("^c#222222^^b#8ec07c^   %d%% ^d^", capacidad);

    return 0;
}



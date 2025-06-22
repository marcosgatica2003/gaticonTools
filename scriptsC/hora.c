#include <stdio.h>
#include <time.h>

int main() {
    time_t ahora = time(NULL);
    struct tm * tm_struct = localtime(&ahora);
    int hora = tm_struct->tm_hour;
    int minutos = tm_struct->tm_min;

    printf("^c#222222^^b#e9d9b0^ %02d:%02d ^d^", hora, minutos);
    return 0;
}



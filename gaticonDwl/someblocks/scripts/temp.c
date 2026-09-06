#include <stdio.h>

#define MAX_PATH_SIZE 256
int main(void) {
    
    char path[MAX_PATH_SIZE] = {0};
    snprintf(path, sizeof(path), "/run/hwmon-k10temp/temp1_input");

    FILE* fp = fopen(path, "r");
    if (!fp) { perror("fopen"); return 1; }

    unsigned int temp = 0;
    if (fscanf(fp, "%d", &temp) != 1) {
        fprintf(stderr, "Error al leer\n");
        fclose(fp); return 1;
    }

    fclose(fp);
    printf(" +%d.%d C \n", temp/1000, (temp % 1000) / 100);

    return 0;
}

#include <stdio.h>

#define MAX_PATH_SIZE 256
int main(int argc, char* argv[]) {
    
    if (argc != 2) {
        fprintf(stderr, "Uso: %s hwmonx\n", argv[0]);
        return 1;
    }

    char path[MAX_PATH_SIZE] = {0};
    snprintf(path, sizeof(path), "/sys/class/hwmon/%s/temp1_input", argv[1]);

    FILE* fp = fopen(path, "r");
    if (!fp) { perror("fopen"); return 1; }

    unsigned int temp = 0;
    if (fscanf(fp, "%d", &temp) != 1) {
        fprintf(stderr, "Error al leer\n");
        fclose(fp); return 1;
    }

    fclose(fp);
    printf("^c#fb4934^ +%d.%d C ^d^\n", temp/1000, (temp % 1000) / 100);

    return 0;
}

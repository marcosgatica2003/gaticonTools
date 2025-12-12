#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

#define TEMP_SENSOR "/run/hwmon-k10temp/temp1_input"
#define PWM1 "/run/hwmon-dell/pwm1"
#define PWM2 "/run/hwmon-dell/pwm2"
#define SLEEP_US 500000

typedef struct {
    float* temps;
    int size;
    int count;
    int idx;
} tempHistory;

float readTemp(void);
int calcPwm(float, float, float, int, int);
void writePwm(int);
void initHistory(tempHistory*, int);
void addTemp(tempHistory*, float);
float avgTemp(tempHistory*);

int main(int argc, char* argv[]) {
    if (argc < 3 || argc > 6) {
        printf("Uso: %s <tempMin> <tempMax> [minPwm] [maxPwm] [average]\n", argv[0]);
        printf("Ejemplo: %s 10 60 50 255 5\n", argv[0]);
        printf(" minPwm = PWM mínimo (default: 0)\n");
        printf(" maxPwm = PWM máximo (default: 255)\n");
        printf(" average: número de muestras a promediar (default: 1)\n");
        return 1; 
    }

    float tMin = atof(argv[1]);
    float tMax = atof(argv[2]);
    int minPwm = (argc > 3) ? atoi(argv[3]) : 0;
    int maxPwm = (argc > 4) ? atoi(argv[4]) : 255;
    int avgSamples = (argc > 5) ? atoi(argv[5]) : 2;
    if (minPwm < 0 || maxPwm > 255 || minPwm >= maxPwm) {
        fprintf(stderr, "[Error] PWM inválido. Debe ser 0 <= minPwm < maxPwm <= 255\n");
        return 10;
    }
    
    if (tMin >= tMax) {
        fprintf(stderr, "[Error]: temperatura inválida. tempMin < tempMax\n");
        return 1;
    }
    
    if (avgSamples < 1) {
        fprintf(stderr, "[Error] average debe ser >=1\n");
        return 1;
    }
    
    printf("[gaticonFancontrol] Controlando ventiladores...\n");
    printf("  • Tmin = %.1f°C -> PWM=%d\n", tMin, minPwm);
    printf("  • Tmax = %.1f°C -> PWM=%d\n", tMax, maxPwm);
    printf("  • Promediando %d muestra(s)\n", avgSamples);

    tempHistory history;
    initHistory(&history, avgSamples);

    while (1) {
        float tempCurrent = readTemp();
        addTemp(&history, tempCurrent);
        float tempAvg = avgTemp(&history);
        int pwm = calcPwm(tempAvg, tMin, tMax, minPwm, maxPwm);
        writePwm(pwm);
        printf("T=%5.1fºC (avg=%5.1fºC) -> PWM=%3d\r", tempCurrent, tempAvg, pwm);
        fflush(stdout);
        usleep(SLEEP_US);
    }

    free(history.temps);
    return 0;
}

float readTemp(void) {
    FILE* f= fopen(TEMP_SENSOR, "r");
    if (!f) { perror("Error al abrir el sensor"); exit(1); }
    int raw = 0;
    fscanf(f, "%d", &raw);
    fclose(f);
    return raw / 1000.0;
}

int calcPwm(float temp, float tMin, float tMax, int minPwm, int maxPwm) {
    if (temp <= tMin) return minPwm;
    if (temp <= tMax) return maxPwm;

    float ratio = (temp - tMin) / (tMax - tMin);
    return (int)(minPwm + ratio * (maxPwm - minPwm));
}

void writePwm(int value) {
    FILE* f;
    f = fopen(PWM1, "w");
    if (f) { fprintf(f, "%d", value); fclose(f); 
    } else {
        fprintf(stderr, "[Error] Escribiendo en %s\n", PWM1);
    }
    f = fopen(PWM2, "w");
    if (f) { fprintf(f, "%d", value); fclose(f); 
    } else {
        fprintf(stderr, "[Error] Escribiendo en %s\n", PWM2);
    }
}

void initHistory(tempHistory* h, int size) {
    h->temps = malloc(size * sizeof(float));
    h->size = size;
    h->count = 0;
    h->idx = 0;
}

void addTemp(tempHistory* h, float temp) {
    h->temps[h->idx] = temp;
    h->idx = (h->idx + 1) % h->size;
    if (h->count < h->size) h->count++;
}

float avgTemp(tempHistory* h) {
    float sum = 0;
    for (int i = 0; i < h->count; i++) {
        sum += h->temps[i];
    }

    return sum / h->count;
}



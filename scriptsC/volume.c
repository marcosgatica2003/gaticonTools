#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define MAX_BUF_SIZE 256

int ejecutar(const char*, char*, size_t);
int estaMuteado();
void getVolumen(char*, size_t);
void click(int);

int main() {
    char volume[MAX_BUF_SIZE];
    char* blockButton = getenv("BLOCK_BUTTON");

    if (blockButton != NULL) {
        click(atoi(blockButton));
    }
    if ( estaMuteado() ) { printf("OFF\n"); }
    else {
        getVolumen(volume, MAX_BUF_SIZE);
        printf("%s\n", volume);
    }
    return 0;
}

int ejecutar(const char* cmd, char* output, size_t outputSize) {

    FILE* fp;

    fp = popen(cmd, "r");
    if (fp == NULL) { return -1; }

    if (fgets(output, outputSize, fp) == NULL) { 
        pclose(fp); 
        return -1; 
    }

    size_t len = strlen(output);
    if (len > 0 && output[len-1] == '\n') { output[len-1] = '\0'; }

    pclose(fp);
    return 0;
}

int estaMuteado() {
    char buffer[MAX_BUF_SIZE];

    if(ejecutar("pactl get-sink-mute @DEFAULT_SINK@ | grep 'no'", buffer, MAX_BUF_SIZE) == 0) { return 0; } //desmuteado
    return 1; //muteado
}

void getVolumen(char* volume, size_t volumeSize) {
    char buffer[MAX_BUF_SIZE];

    if(ejecutar("pactl get-sink-volume @DEFAULT_SINK@ | grep -o '[0-9]\\+%' | head -1", buffer, MAX_BUF_SIZE) == 0) {
        strncpy(volume, buffer, volumeSize);
        volume[volumeSize-1] = '\0';
    } else {
        strncpy(volume, "?%", volumeSize);
        volume[volumeSize-1] = '\0';
    }
}

void click(int button) {
    switch (button) {
        case 1:
            system("pactl set-sink-mute @DEFAULT_SINK@ toggle");
            break;
        case 3:
            system("GTK_THEME='Adwaita:dark' pavucontrol &");
            break;
        case 4:
            system("pactl set-sink-volume @DEFAULT_SINK@ +5%");
            break;
        case 5:
            system("pactl set-sink-volume @DEFAULT_SINK@ -5%");
            break;
    }
}


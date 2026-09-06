#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define WINDOW_TITLE_SIZE 512

int main() {
    FILE* fp = popen("xdotool getactivewindow getwindowclassname 2>/dev/null", "r");
    
    if (!fp) return 1;

    char windowTitle[WINDOW_TITLE_SIZE];
    if (!fgets(windowTitle, sizeof(windowTitle), fp)) {
        pclose(fp); 
        return 1;
    }
    
    pclose(fp);
    size_t len = strlen(windowTitle);
    if (len && windowTitle[len-1] == '\n') {
        windowTitle[len-1] = '\0';
        --len;
    }

    const size_t totalLength = 200;
    size_t paddingLength = (len < totalLength) ? (totalLength - len) : 1;

    printf("%s\n", windowTitle);
    for (size_t i = 0; i < paddingLength; ++i) {
        putchar(' ');
    }
    putchar('\n');

    return 0;
}



static const Block blocks[] = {
	/*Icon*/	/*Command*/		/*Update Interval*/	/*Update Signal*/
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/redCircle",   -1, 0},
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/yellowCircle",   -1, 0},
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/greenCircle",   -1, 0},
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/volume",  2,  1},
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/internet.py", 30,  2},
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/battery", 5, 3},
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/hora", 5,   0},
};

//sets delimiter between status commands. NULL character ('\0') means no delimiter.
static char delim[] = "\0";
static unsigned int delimLen = 5;

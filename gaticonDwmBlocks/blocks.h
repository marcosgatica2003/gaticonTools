static const Block blocks[] = {
	/*Icon*/	/*Command*/		/*Update Interval*/	/*Update Signal*/
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/volume",  2,  1},
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/internet.py", 5,  2},
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/battery", 30, 3},
    {"^c#222222^^b#e9d9b0^ ",    "date '+%I:%M%p' ^d^", 5,   0},
};

//sets delimiter between status commands. NULL character ('\0') means no delimiter.
static char delim[] = "^c#222222^ | ^d^";
static unsigned int delimLen = 10;

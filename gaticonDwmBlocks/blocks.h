static const Block blocks[] = {
	/*Icon*/	/*Command*/		/*Update Interval*/	/*Update Signal*/
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/volume",  2,  1},
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/dist/internet/internet", 30,  2},
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/battery", 5, 3},
    {"",    "/home/marcosgatica/.config/dwmblocks/scripts/hora", 5,   0},
};

//sets delimiter between status commands. NULL character ('\0') means no delimiter.
static char delim[] = "\0";
static unsigned int delimLen = 5;

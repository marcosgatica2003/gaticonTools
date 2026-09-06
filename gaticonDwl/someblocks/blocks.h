//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/		/*Update Interval*/	/*Update Signal*/
	{"",    "/home/marcosgatica/Repositorios/gaticonTools/gaticonDwl/someblocks/scripts/temp",  5,   0},
    {"",    "/home/marcosgatica/Repositorios/gaticonTools/gaticonDwl/someblocks/scripts/internet.py",   30, 0},
    {"",    "/home/marcosgatica/Repositorios/gaticonTools/gaticonDwl/someblocks/scripts/volume",    0,  0},
    {"",    "/home/marcosgatica/Repositorios/gaticonTools/gaticonDwl/someblocks/scripts/battery",   5,  0},
    {"",    "/home/marcosgatica/Repositorios/gaticonTools/gaticonDwl/someblocks/scripts/hora",  15,  0},


    /* {"",    "echo 'funciona 1'",	30,		0}, */

	/* {"", "date '+%b %d (%a) %I:%M%p'",					5,		0}, */
	
	/* Updates whenever "pkill -SIGRTMIN+10 someblocks" is ran */
	/* {"", "date '+%b %d (%a) %I:%M%p'",					0,		10}, */
};



//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim[] = ">";
static unsigned int delimLen = 5;

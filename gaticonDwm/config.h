/* See LICENSE file for copyright and license details. */

#define BAR_HEIGHT 16

/* appearance */
/* #include <cstddef> */
static const unsigned int borderpx  = 1;        /* border pixel of windows */

static const unsigned int systraypinning = 0;   /* 0: sloppy systray follows selected monitor, >0: pin systray to monitor X */
static const unsigned int systrayonleft = 0;    /* 0: systray in the right corner, >0: systray on left of status text */
static const unsigned int systrayspacing = 2;   /* systray spacing */
static const int systraypinningfailfirst = 1;   /* 1: if pinning fails, display systray on the first monitor, False: display systray on the last monitor*/
static const int showsystray        = 1;        /* 0 means no systray */

static const unsigned int snap      = 12;       /* snap pixel */
static const int showbar            = 1;        /* 0 means no bar */
static const int topbar             = 1;        /* 0 means bottom bar */
static const unsigned int gappih =  7;
static const unsigned int gappiv =  8;
static const unsigned int gappoh =  8;
static const unsigned int gappov =  8;
static int smartgaps = 0;
static const char *fonts[]          = { "JetBrainsMonoNerdFont:style=Regular:size=10" };
static const int refreshrate = 120;
static const char col_fg_norm[]     = "#928374"; 
static const char col_bg_norm[]     = "#222222";
static const char col_border_norm[] = "#222222";

static const char col_fg_sel[]      = "#ebdbb2";
static const char col_bg_sel[]      = "#222222";
static const char col_border_sel[]  = "#cc241d";

static const char col_urgent[]      = "#f0c674";
static const char col_black[]       = "#000000";

static const char *colors[][3]      = {
    /*               fg            bg            border         */
    [SchemeNorm] = { col_fg_norm,  col_bg_norm,  col_border_norm },
    [SchemeSel]  = { col_fg_sel,   col_bg_sel,   col_border_sel  },
};

/* tagging */
static const char *tags[] = { "1", "2", "3", "4", "5"};

static const Rule rules[] = {
	/* xprop(1):
	 *	WM_CLASS(STRING) = instance, class
	 *	WM_NAME(STRING) = title
	 */
	/* class      instance    title       tags mask     isfloating   monitor */
	{ "feh",     NULL,       NULL,       0,            1,           -1 },
	{ "mpv",     NULL,       NULL,       0,            1,           -1 },
	{ "mplayer",     NULL,       NULL,       0,            1,           -1 },
	/* { "Firefox",  NULL,       NULL,       1 << 8,       0,           -1 }, */
    /* { "Plank", "plank", NULL, ~0, 1, -1 }, */
};

/* layout(s) */
static const float mfact     = 0.55; /* factor of master area size [0.05..0.95] */
static const int nmaster     = 1;    /* number of clients in master area */
static const int resizehints = 1;    /* 1 means respect size hints in tiled resizals */
static const int lockfullscreen = 1; /* 1 will force focus on the fullscreen window */

#define FORCE_VSPLIT 1

#include "vanitygaps.c"

static const Layout layouts[] = {
	/* symbol     arrange function */
	{ "",      tile },    /* first entry is default */
	{ "",      monocle },
	{ "[@]",      spiral },
	{ "[\\]",     dwindle },
	{ "",      deck },
	{ "TTT",      bstack },
	{ "===",      bstackhoriz },
	{ "HHH",      grid },
	{ "###",      nrowgrid },
	{ "---",      horizgrid },
	{ ":::",      gaplessgrid },
	{ "|M|",      centeredmaster },
	{ ">M>",      centeredfloatingmaster },
	{ "><>",      NULL },    /* no layout function means floating behavior */
	{ NULL,       NULL },
};


/* key definitions */
#define MODKEY Mod4Mask
/* #define MODKEY_ALT Mod1Mask */

/* #define TAGKEYS_ALT(KEY,TAG) \ */
/* 	{ MODKEY_ALT,                       KEY,      view,           {.ui = 1 << TAG} }, \ */
/* 	{ MODKEY_ALT|ControlMask,           KEY,      toggleview,     {.ui = 1 << TAG} }, \ */
/* 	{ MODKEY_ALT|ShiftMask,             KEY,      tag,            {.ui = 1 << TAG} }, \ */
/* 	{ MODKEY_ALT|ControlMask|ShiftMask, KEY,      toggletag,      {.ui = 1 << TAG} }, */

#define TAGKEYS(KEY,TAG) \
	{ MODKEY,                       KEY,      view,           {.ui = 1 << TAG} }, \
	{ MODKEY|ControlMask,           KEY,      toggleview,     {.ui = 1 << TAG} }, \
	{ MODKEY|ShiftMask,             KEY,      tag,            {.ui = 1 << TAG} }, \
	{ MODKEY|ControlMask|ShiftMask, KEY,      toggletag,      {.ui = 1 << TAG} },

/* commands */
static char dmenumon[2] = "0"; /* component of dmenucmd, manipulated in spawn() */
static const char *dmenucmd[] = { "/usr/local/bin/dmenu_run", NULL };
static const char *termcmd[]  = { "/usr/local/bin/st","-e", "/bin/tmux", NULL };
static const char *capturadorPantalla[] = { "/home/marcosgatica/Repositorios/gaticonTools/capturadorDePantallas/gaticonCaptureX11", NULL};
/* static const char *temperaturasConRofi[] = { "/home/marcosgatica/.config/rofi/temperaturas.sh", NULL }; */
static const char *tabbedScript[] = { "/home/marcosgatica/.config/utilidadesYSistema/scripts/toggleTabbed.sh", NULL };
/* static const char *traycmd[] = { "/home/marcosgatica/.config/dwmblocks/scripts/trayerControl.sh", NULL }; */

#include "movestack.c"
static const Key keys[] = {
	/* modifier                     key        function        argument */
    { MODKEY,                       XK_s,       togglesticky,   {0} },
	{ MODKEY,                       XK_d,      spawn,          {.v = dmenucmd } },
    /* { MODKEY|ShiftMask,             XK_d,      spawn,          {.v = traycmd} }, */
	{ MODKEY,                       XK_Return, spawn,          {.v = termcmd } },
    { MODKEY,                       XK_c,       spawn,          {.v = capturadorPantalla}},
    /* { MODKEY,                       XK_t,       spawn,          {.v = temperaturasConRofi}}, */
	{ MODKEY,                       XK_Right,      focusstack,     {.i = +1 } },
	{ MODKEY,                       XK_Left,      focusstack,     {.i = -1 } },
    { MODKEY,                       XK_w,       setlayout,      {.v = &layouts[1]}},
    { MODKEY|ShiftMask,             XK_w,      spawn,          { .v = tabbedScript }},
	{ MODKEY,                       XK_h,      setmfact,       {.f = -0.05} },
    { MODKEY|ShiftMask,             XK_j,      movestack,      {.i = +1} },
    { MODKEY|ShiftMask,             XK_k,      movestack,      {.i = -1} },
	{ MODKEY,                       XK_l,      setmfact,       {.f = +0.05} },
	{ MODKEY|ShiftMask,             XK_q,      killclient,     {0} },
	{ MODKEY,                       XK_e,      setlayout,      {.v = &layouts[0]} },
	{ MODKEY,                       XK_space,  setlayout,      {0} },
	{ MODKEY,                       XK_Down,   moveresize,     {.v = "0x 25y 0w 0h" } },
	{ MODKEY,                       XK_Up,     moveresize,     {.v = "0x -25y 0w 0h" } },
	{ MODKEY,                       XK_Right,  moveresize,     {.v = "25x 0y 0w 0h" } },
	{ MODKEY,                       XK_Left,   moveresize,     {.v = "-25x 0y 0w 0h" } },
	{ MODKEY|ShiftMask,             XK_Down,   moveresize,     {.v = "0x 0y 0w 25h" } },
	{ MODKEY|ShiftMask,             XK_Up,     moveresize,     {.v = "0x 0y 0w -25h" } },
	{ MODKEY|ShiftMask,             XK_Right,  moveresize,     {.v = "0x 0y 25w 0h" } },
	{ MODKEY|ShiftMask,             XK_Left,   moveresize,     {.v = "0x 0y -25w 0h" } },
	{ MODKEY|ShiftMask,             XK_space,  togglefloating, {0} },
	{ MODKEY,                       XK_0,      view,           {.ui = ~0 } },
	{ MODKEY|ShiftMask,             XK_0,      tag,            {.ui = ~0 } },
	{ MODKEY,                       XK_comma,  focusmon,       {.i = -1 } },
	{ MODKEY,                       XK_period, focusmon,       {.i = +1 } },
	{ MODKEY|ShiftMask,             XK_comma,  tagmon,         {.i = -1 } },
	{ MODKEY|ShiftMask,             XK_period, tagmon,         {.i = +1 } },
	TAGKEYS(                        XK_1,                      0)
	TAGKEYS(                        XK_2,                      1)
	TAGKEYS(                        XK_3,                      2)
	TAGKEYS(                        XK_4,                      3)
	TAGKEYS(                        XK_5,                      4)
	/* TAGKEYS(                        XK_6,                      5) */
	/* TAGKEYS(                        XK_7,                      6) */
	/* TAGKEYS(                        XK_8,                      7) */
	/* TAGKEYS(                        XK_9,                      8) */

    /* TAGKEYS_ALT(                        XK_1,                      5) */
	/* TAGKEYS_ALT(                        XK_2,                      6) */
	/* TAGKEYS_ALT(                        XK_3,                      7) */
	/* TAGKEYS_ALT(                        XK_4,                      8) */
};

/* button definitions */
/* click can be ClkTagBar, ClkLtSymbol, ClkStatusText, ClkWinTitle, ClkClientWin, or ClkRootWin */
static const Button buttons[] = {
	/* click                event mask      button          function        argument */
	{ ClkLtSymbol,          0,              Button1,        setlayout,      {0} },
	{ ClkLtSymbol,          0,              Button3,        setlayout,      {.v = &layouts[2]} },
	{ ClkWinTitle,          0,              Button2,        zoom,           {0} },
	{ ClkStatusText,        0,              Button2,        spawn,          {.v = termcmd } },
	{ ClkClientWin,         MODKEY,         Button1,        movemouse,      {0} },
	{ ClkClientWin,         MODKEY,         Button2,        togglefloating, {0} },
	{ ClkClientWin,         MODKEY,         Button3,        resizemouse,    {0} },
	{ ClkTagBar,            0,              Button1,        view,           {0} },
	{ ClkTagBar,            0,              Button3,        toggleview,     {0} },
	{ ClkTagBar,            MODKEY,         Button1,        tag,            {0} },
	{ ClkTagBar,            MODKEY,         Button3,        toggletag,      {0} },
};


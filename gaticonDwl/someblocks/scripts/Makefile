BINARIOS = battery greenCircle hora redCircle titulos volume yellowCircle

CC = gcc
CFLAGS = -Wall -Wextra -O2

all: $(BINARIOS)

$(BINARIOS):
	$(CC) $(CFLAGS) $@.c -o $@

clean:
	rm -f $(BINARIOS)

.PHONY: all clean

CFLAGS?=-std=c99 -Wall -Wextra -pedantic
CC=gcc
PROGRAMS=part1 part2


all: $(PROGRAMS)

%: %.c
	$(CC) $^ -o $@ $(CFLAGS)

clean:
	rm -f $(PROGRAMS) 


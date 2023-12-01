#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <ctype.h>

#define MAXLINE 1024



int first_digit(char *line) {
    for (size_t i = 0; i < strlen(line); i++) {
        if (isdigit(line[i])) {
            return (int)(line[i] - '0');
        }
    }
    printf("err\n");
    exit(1);
}


int last_digit(char *line) {
    printf("Last digit scanning...\n");
    int i = strlen(line) - 1;
    while (i >= 0) {
        if (isdigit(line[i])) {
            return (int)(line[i] - '0');
        }
        i--;
    }
    printf("err\n");
    exit(1);
}



int find_cal_val_on_line(char *line) {
    int localsum = 0;
    localsum += first_digit(line);
    localsum = localsum * 10 + last_digit(line);
    printf("Adding to sum: %d\n", localsum);
    return localsum;

}


int main(int argc, char **argv) {
    argv[0] = argv[0]; //To supress compiler warning
    assert(argc == 1);

    FILE *fp = fopen("input.txt", "r");
    assert(fp != NULL);

    char *line = NULL;
    size_t bufsize = 100;

    int sum = 0;

    while(getline(&line, &bufsize, fp) != -1) {
        sum += find_cal_val_on_line(line);
    }
    printf("Sum: %d\n", sum);

    fclose(fp);
    free(line);

    return 0;
}

#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <ctype.h>

#define MAXLINE 1024

const char *digits[] = {
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"
};


int word_to_digit(char *word) {
    for (size_t i = 0; i < 9; i++) {
        if (strcmp(word, digits[i]) == 0) {

            return i+1;
        }
    }
    printf("err word to digit\n");
    exit(1);
}


int first_digit(char *line) {
    char found[24];
    for (size_t i = 0; i < strlen(line); i++) {
        for (size_t j = 0; j < 18; j++) {
            char *res = strnstr(line, digits[j], i);
            if (res != NULL) {
                strncpy(found, res, strlen(digits[j]));
                found[strlen(digits[j])] = '\0';
                if (strlen(found) == (size_t)1) { //means it is a word
                    return (int)(found[0] - '0');
                } else {
                    //return 1;
                    return word_to_digit(found); //Means it is indeed a digit
                }
            }
        }
    }
    printf("err\n");
    exit(1);
}

int last_digit(char *line) {
    char found[24];
    for (int i = strlen(line) - 1; i >= 0; i--) {
        for (size_t j = 0; j < 18; j++) {
            char *res = strnstr(&line[i], digits[j], strlen(line) - i);
            if (res != NULL) {
                strncpy(found, res, strlen(digits[j]));
                found[strlen(digits[j])] = '\0';
                printf("Line %s, Found: %s, i: %d, j: %ld, strelen digits j: %ld\n ", line, found, i, j, strlen(digits[j]));
                if (strlen(found) == (size_t)1) { //means it is a word
                    return (int)(found[0] - '0');
                } else {
                    //return 1;
                    return word_to_digit(found); //Means it is indeed a digit
                }
            }
        }
    }
    printf("err\n");
    exit(1);
}


int find_cal_val_on_line(char *line) {
    int localsum = 0;
    localsum += first_digit(line);
    localsum = localsum * 10 + last_digit(strdup(line));
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

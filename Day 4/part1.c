#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

#define MAXLINE 1024

int card_sum(char* card) {
    
    int num_wins_on_card = 1;
    int card_num;
    char winning[MAXLINE];
    char actual[MAXLINE];
    int result = sscanf(card, "Card %d: %[0-9 ] | %[0-9 ]", &card_num, winning, actual);
    assert(result > 0);

    char *win_ptr; 
    char *winner_num = strtok_r(winning, " ", &win_ptr);
    while (winner_num != NULL) {
        int num1 = atoi(winner_num);
        char *num_ptr;
        char *num = strtok_r(strdup(actual), " ", &num_ptr);
        while (num != NULL) {
            int num2 = atoi(num);

            if (num1 == num2) {
                printf("Num %d is in both strs\n", num1);
                num_wins_on_card *= 2; //We can save code by having doubled on time too much initially
            }

            num = strtok_r(NULL, " ", &num_ptr);
        }

        winner_num = strtok_r(NULL, " ", &win_ptr);
    }

    if (!num_wins_on_card) {
        return 0;
    } else {
        return num_wins_on_card/2; //To account for 1 init mult
    }

    
}


int main(int argc, char **argv) {
    argv[0] = argv[0]; //To supress compiler warning

    assert(argc == 2);

    FILE *fp = fopen(argv[1], "r");

    char *line = NULL;
    size_t bufsize = MAXLINE;

    int pile_sum = 0;
    while(getline(&line, &bufsize, fp) != -1) {
        pile_sum += card_sum(line);
    }
    printf("Total sum %d\n", pile_sum);

    fclose(fp);
    free(line);

    return 0;
}

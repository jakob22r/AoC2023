#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

#define MAXLINE 1024

//Returns num of wins on a card, important to use reintrant version of strtok
int card_wins(char* card) {
    
    int num_wins_on_card = 0;
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
                num_wins_on_card++; 
            }
            num = strtok_r(NULL, " ", &num_ptr);
        }
        winner_num = strtok_r(NULL, " ", &win_ptr);
    }
    return num_wins_on_card;
}

//Recursive function to calculate the contribution of the i'th component and storing in the dp talbe
//Number of wins on a card is preprocessed and stored in the array of cards
int calc_score(int i, int *dp, char* cards) {
    if (dp[i] != -1) {
        return dp[i];
    } 
    int score = 1;
    for (int j = i+1; j < i+1+cards[i]; j++) {
        score += calc_score(j, dp, cards);
    }
    dp[i] = score; //Total contribution for the i'th card
    return score;
}

int main(int argc, char **argv) {
    argv[0] = argv[0]; //To supress compiler warning

    assert(argc == 2);

    FILE *fp = fopen(argv[1], "r");

    size_t lineCount = 0;
    char buffer[MAXLINE]; 

    while (fgets(buffer, sizeof(buffer), fp) != NULL) {
        lineCount++;
    }
    rewind(fp);

    char *line = NULL;
    size_t bufsize = MAXLINE;

    //Add initial card wins into table, i.e. preprocess
    char *cards = malloc(sizeof(int) * lineCount); 
    int i = 0;
    while(getline(&line, &bufsize, fp) != -1) {
        cards[i] = card_wins(line); //Table over initial wins 
        i++;
    }

    //Initialize a dynamic programming table
    int *dp = malloc(sizeof(int) * lineCount); 
    for (size_t j = 0; j < lineCount; j++) {
        dp[j] = -1;
    }
    
    //Call dp algoritm getscore
    int total_score = 0;
    for (size_t i = 0; i < lineCount; i++) {
        //Will calculate the total contribution of Card 1
        total_score += calc_score(i, dp, cards);
    }
    printf("Total score %d\n", total_score);
    
    fclose(fp);
    free(dp);
    free(line);
    free(cards);

    return 0;
}

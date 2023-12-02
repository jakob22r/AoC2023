#include <stdlib.h>
#include <stdio.h>
#include <assert.h>
#include <string.h>

#define MAXLINE 1024

//Returns 0 if game is not possible and otherwise the appropiate sum
//Assumed configuration is bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes
int get_game_sum(char* line) {

    int min_reds = 0;
    int min_greens = 0;
    int min_blues = 0;

    int game_num = 0;
    sscanf(line, "Game %d:", &game_num);

    char *colon_pos = strstr(line,":");
    assert(colon_pos != NULL);
    char substr[MAXLINE];
    strcpy(substr, colon_pos+1);

    char *saveptr1;
    char *token = strtok_r(substr,";",&saveptr1);
    //Split into tokens for each set revealed, use reentrant version of strtok
    while (token != NULL) {

        char *token_copy = strdup(token);
        
        // //Extract colors in that draw
        char *saveptr2;
        char *sub_token = strtok_r((token_copy),",", &saveptr2);
        while (sub_token != NULL) {

            //Find out where to add
            int amount = 0;
            char color[MAXLINE];
            sscanf(sub_token, "%d %s", &amount, color);

            //Update min variable if applicable
            if ((strcmp(color, "red") == 0) && amount > min_reds) {
                min_reds = amount;
            } else if ((strcmp(color, "green") == 0) && amount > min_greens) {
                min_greens = amount;
            } else if ((strcmp(color, "blue") == 0) && amount > min_blues) {
                min_blues = amount;
            }
            //Next color in that draw
            sub_token = strtok_r(NULL,",", &saveptr2);
        }
        free(token_copy);
        //Next draw
        token = strtok_r(NULL,";",&saveptr1);
    }
    return (min_reds * min_greens * min_blues);
}



int main(int argc, char **argv) {
    argv[0] = argv[0]; //To supress compiler warning

    assert(argc == 1);

    FILE *fp = fopen("sample.txt", "r");

    char *line = NULL;
    size_t bufsize = MAXLINE;

    int id_sum = 0;
    int cnt = 1;
    while(getline(&line, &bufsize, fp) != -1) {
        int res = get_game_sum(line);
        printf("Adding for game %d is %d\n", cnt, res);
        id_sum += res;
        cnt++;
    }
    printf("Sum: %d", id_sum);
    fclose(fp);
    free(line);

    return 0;
}

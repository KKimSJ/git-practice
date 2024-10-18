#include <stdio.h>
#include <string.h>

int main() {
    char input[256];

    printf("Enter the string: ");
    fgets(input, sizeof(input), stdin);

    int hong_len = 4;
    int dong_len = 4;

    for (int i = 0; input[i] != '\0'; i++) {
        if (input[i] == 'h' && input[i + 1] == 'o' && input[i + 2] == 'n' && input[i + 3] == 'g') {
            if (i == 0 || input[i - 1] == ' ') {
                if (input[i + hong_len] == ' ') {
                    for (int j = i + hong_len + 1; input[j] != '\0'; j++) {
                        if (input[j] == 'd' && input[j + 1] == 'o' && input[j + 2] == 'n' && input[j + 3] == 'g') {
                            if (j == 0 || input[j - 1] == ' ') {
                                if (input[j + dong_len] == ' ' || input[j + dong_len] == '\0') {
                                    int space_count = 0;
                                    int word_count = 0;
                                    char word[50];
                                    int word_index = 0;

                                    for (int k = i + hong_len + 1; k < j; k++) {
                                        if (input[k] == ' ') {
                                            space_count++;
                                            if (word_index > 0) {
                                                word[word_index] = '\0';
                                                word_count++;
                                                word_index = 0;
                                            }
                                        }
                                        else {
                                            word[word_index++] = input[k];
                                        }
                                    }
                                    if (word_index > 0) {
                                        word[word_index] = '\0';
                                        word_count++;
                                    }

                                    if (word_count == 1) {
                                        printf("hong %s dong\n", word);
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    return 0;
}

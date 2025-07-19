#include <stdio.h>
#include <string.h>

int main() {
    char str[100];
    int i, len, word = 1;

    printf("Enter a string: ");
    scanf("%[^\n]s", str); // Read string until newline
    
    len = strlen(str);
    
    // Count words (assuming words are separated by spaces)
    for(i = 0; i < len; i++) {
        if(str[i] == ' ' && str[i+1] != ' ' && str[i+1] != '\0') {
            word++;
        }
    }
    
    printf("Number of words: %d\n", word);
    
    return 0;
}
#include <stdio.h>
#include <string.h>
/* Made by: Encrypted, leon and AJblu */
char alphabet[86] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3',
    '4', '5', '6', '7', '8', '9', '0'
    };

int leng;

int main(){



    int input;

    printf("[---------- Welcome to the xt32 encoder by 5/9Dark. ------------]\n|                                                               |\n|                                                               |\n|                                                               |\n|                                                               |\n|             1.) Encode              2.) Decode                |\n|                  * Make sure to set shift!                    |\n|                  [ (C) 2020 FiveNineDark ]                    |\n[---------------------------------------------------------------]\n\n\n\n");

    printf("[+] Select your option: ");
    scanf("%d%*c", &input);

    if(input == 1){
        str_encode();
    }

    else if(input == 2){
        str_decode();
    }

    return 0;
}

void str_encode(){
    char string[100];
    char key[100];

    printf("[+] String to encode: ");
    fgets(string, 100, stdin);
    printf("[+] Key to string: ");
    fgets(key, 100, stdin);

    for(int i = 0; i < 86; i++){
        leng = strlen(key);
        char lett = alphabet[i];
        printf("%c", lett);
        for(int x = 0; x < leng; x++){
        //if key[x] == lett{
        //do stuff}
        };
    };

}

void str_decode(){
    char string_dec[100];
    int key_dec[100];

    printf("[+] Enter string to decode: ");
    fgets(string_dec, 100, stdin);
    printf("[+] Key to string: ");
    fgets(key_dec, 100, stdin);

}

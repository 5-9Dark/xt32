#include <stdio.h>
/* Made by: Encrypted, leon and AJblu */

int main(){

    int input;

    printf("[---------- Welcome to the xt32 encoder by 5/9Dark. ------------]\n|                                                               |\n|   * Make sure to set shift!                                   |\n|                                                               |\n|                                                               |\n|             1.) Encode              2.) Decode                |\n|                                                               |\n|                  [ (C) 2020 FiveNineDark ]                    |\n[---------------------------------------------------------------]\n\n\n\n");
    printf("[+] Select your option: ");
    scanf("%d", &input);

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
    scanf("%d", &string);
    printf("[+] Key to string: ");
    scanf(" %d", &key);

}

void str_decode(){
    char string_dec[100];
    int key_dec[100];

    printf("[+] Enter string to decode: ");
    scanf("%d", &string_dec);
    printf("[+] Key to string: ");
    scanf(" %d", &key_dec);

}

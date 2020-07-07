#include <stdio.h>

int main(){

    str_encode();
    str_decode();

    return 0;
}

void str_encode(){
    char string[100];
    char key[100];

    printf("[+] String to encode: ");
    scanf("%c", &string);
    printf("[+] Key to string: ");
    scanf(" %c", &key);

}

void str_decode(){
    char string_dec[100];
    int key_dec[100];

    printf("[+] Enter string to decode: ");
    scanf("%c", &string_dec);
    printf("[+] Key to string: ");
    scanf("%d", &key_dec);




}


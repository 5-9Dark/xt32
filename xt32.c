#include <stdio.h>

int main( int argc, char *argv[] ) {

   if( argc == 2 ) {
      printf("The argument supplied is %s\n", argv[1]);
   }
   if( argc == "help" ) {
      printf("xt32: Test.\n");
   }
   else {
      printf("xt32: Argument not expected...\n\n");
   }


}

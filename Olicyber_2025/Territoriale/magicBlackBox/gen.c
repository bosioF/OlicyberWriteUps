#include <stdlib.h>
#include <stdio.h>

int main() {
    srand(0x1337);
    for (int i = 0; i < 0x2000; i++) {
        printf("%d, ", rand());
    }
}

//gcc -o gen gen.c -> ./gen > nums.txt
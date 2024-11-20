#include <stdio.h>
int main() {
    int a, b;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    if (a >= b) {
        printf("Invalid input: Ensure the first number is smaller than the second number.\n");
        return 1;
    }
    for (int i = a; i <= b; i++) {
        if (i % 5 == 0 && i % 7 == 0) {
            printf("FooBar ");
        } else if (i % 5 == 0) {
            printf("Foo ");
        } else if (i % 7 == 0) {
            printf("Bar ");
        } else {
            printf("Baz "); 
        }
          printf("\n"); 
    }
    return 0;
}

#include <stdio.h>
int main() {
    int arr[100];
    int n,i;
    int sum=0;

    printf("Enter size of the array: ");
    scanf("%d",&n);

    printf("Enter numbers: ");
    for(i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }

    for(i=0; i<n; i++) {
        if(arr[i]>0) {
            sum+=arr[i];
        }
    }
    printf("Sum of positive numbers: %d", sum);
    return 0;
}

#include <stdio.h>
#include <stdlib.h>

// Bubble sort algorithm (O(N^2)) added via Evolution Knowledge Base
void bubble_sort(int arr[], int n) {
    int i, j, temp;
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}


int main() {
    // [AI Generated Logic from Intent]
    int arr[] = {42, 17, 93, 8, 26, 11};
    int n = sizeof(arr)/sizeof(arr[0]);
    
    // Invoke capability from array_sort.skill
    bubble_sort(arr, n);
    
    printf("Sorted array by Evolution Engine: ");
    for(int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}

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


#include <signal.h>
#include <unistd.h>

volatile sig_atomic_t keep_running = 1;
void sig_handler(int sig) {
    printf("\n[C-Kernel Process] Signal caught! Initiating Clean Shutdown Protocol...\n");
    keep_running = 0;
}

int main() {
    // [Hard-Wired Evolution v5.0 Output]
    static const int TEMP = 80;
    static const int MODE = 1;

    // Wiring Handlers for Auto Hot-Swapping
    signal(SIGTERM, sig_handler);
    signal(SIGINT, sig_handler);
    printf("[C-Kernel] Started purely natively. Hardwired TEMP=%d.\n", TEMP);
    while(keep_running) {
        printf("[C-Kernel] Looping / Reading Static Hard-Wired Config. TEMP: %d\r", TEMP);
        fflush(stdout);
        sleep(1);
    }
    printf("\n[C-Kernel] Data-Logic Decoupling complete. Process self-terminated safely.\n");
    return 0;
}

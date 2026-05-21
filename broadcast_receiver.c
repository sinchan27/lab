#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    struct sockaddr_in recvAddr;
    
    memset(&recvAddr, 0, sizeof(recvAddr));
    recvAddr.sin_family = AF_INET;
    recvAddr.sin_port = htons(9090);
    recvAddr.sin_addr.s_addr = htonl(INADDR_ANY);

    bind(sock, (struct sockaddr*)&recvAddr, sizeof(recvAddr));

    char buffer[1024] = {0};
    printf("Waiting for broadcast...\n");
    recvfrom(sock, buffer, 1024, 0, NULL, 0);
    printf("Received: %s\n", buffer);

    close(sock);
    return 0;
}
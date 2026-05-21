#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    int broadcastEnable = 1;
    setsockopt(sock, SOL_SOCKET, SO_BROADCAST, &broadcastEnable, sizeof(broadcastEnable));

    struct sockaddr_in broadcastAddr;
    memset(&broadcastAddr, 0, sizeof(broadcastAddr));
    broadcastAddr.sin_family = AF_INET;
    broadcastAddr.sin_port = htons(9090);
    broadcastAddr.sin_addr.s_addr = inet_addr("255.255.255.255");

    char *msg = "ATTENTION: This is a broadcast message!";
    
    printf("Broadcasting message...\n");
    sendto(sock, msg, strlen(msg), 0, (struct sockaddr*)&broadcastAddr, sizeof(broadcastAddr));
    
    close(sock);
    return 0;
}
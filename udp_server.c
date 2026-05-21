#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8081
#define BUFFER_SIZE 1024

int main() {
    int sockfd;
    char buffer[BUFFER_SIZE];
    char *reply = "Hello Client, UDP Server here!";
    struct sockaddr_in servaddr, cliaddr;
    
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    memset(&servaddr, 0, sizeof(servaddr));
    memset(&cliaddr, 0, sizeof(cliaddr));
    
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(PORT);
    
    bind(sockfd, (const struct sockaddr *)&servaddr, sizeof(servaddr));
    printf("UDP Server waiting for messages on port %d...\n", PORT);
    
    socklen_t len = sizeof(cliaddr);
    int n = recvfrom(sockfd, (char *)buffer, BUFFER_SIZE, MSG_WAITALL, (struct sockaddr *) &cliaddr, &len);
    buffer[n] = '\0';
    printf("Client : %s\n", buffer);
    
    sendto(sockfd, (const char *)reply, strlen(reply), MSG_CONFIRM, (const struct sockaddr *) &cliaddr, len);
    printf("Reply sent.\n");
    
    close(sockfd);
    return 0;
}
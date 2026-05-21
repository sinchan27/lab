#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int server_fd, client_sock;
    struct sockaddr_in server, client;
    socklen_t client_len = sizeof(client);

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(5050);

    bind(server_fd, (struct sockaddr *)&server, sizeof(server));
    listen(server_fd, 5);
    
    printf("Server listening on port 5050...\n");

    client_sock = accept(server_fd, (struct sockaddr *)&client, &client_len);
    
    if (client_sock >= 0) {
        char *client_ip = inet_ntoa(client.sin_addr);
        int client_port = ntohs(client.sin_port);
        
        printf("New client connected!\n");
        printf("Client IP Address : %s\n", client_ip);
        printf("Client Port Number: %d\n", client_port);
    }

    close(client_sock);
    close(server_fd);
    return 0;
}
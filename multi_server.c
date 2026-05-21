#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <pthread.h>

void *connection_handler(void *socket_desc) {
    int sock = *(int*)socket_desc;
    char client_message[2000];
    
    while(recv(sock, client_message, 2000, 0) > 0) {
        printf("Client says: %s", client_message);
        send(sock, client_message, strlen(client_message), 0);
        memset(client_message, 0, 2000);
    }
    
    puts("Client disconnected");
    free(socket_desc);
    return 0;
}

int main() {
    int socket_desc, client_sock, c;
    struct sockaddr_in server, client;
    
    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons(8888);
    
    bind(socket_desc, (struct sockaddr *)&server, sizeof(server));
    listen(socket_desc, 3);
    puts("Multi-client Server waiting for connections...");
    c = sizeof(struct sockaddr_in);
    
    while((client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t*)&c))) {
        puts("Connection accepted");
        
        pthread_t sniffer_thread;
        int *new_sock = malloc(1);
        *new_sock = client_sock;
        
        if(pthread_create(&sniffer_thread, NULL, connection_handler, (void*) new_sock) < 0) {
            perror("Could not create thread");
            return 1;
        }
        pthread_detach(sniffer_thread);
    }
    return 0;
}
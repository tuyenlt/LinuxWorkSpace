#include "learnlib.h"

int dijkstra(std::vector<std::pair<int,int>> *adj,int st,int en,int size){
    int *len = new int(size+1);
    bool *processed = new bool(size+1);
    for(int i=1;i<=size;i++)len[i] = INF;
    len[st] = 0;
    std::queue <int> q;
    q.push(st);
    while(!q.empty()){
        int a = q.front(); q.pop();
        if(processed[a])continue;
        processed[a] = true;
        for(auto u : adj[a]){
            if(len[a] + u.second < len[u.first]){
                len[u.first] = len[a] + u.second;
            }
            q.push(u.first);
        }
    }
    int res = len[en];
    delete len;
    delete processed;
    return res;
}



void makesum_coin(int* c, int n){
    int sum = 0;
    for(int i = 0; i < n; i++)sum += c[i];
    bool *check = new bool(sum+1);
    check[0] = 1;
    for(int k = 0; k < n ; k++){
        for(int i = sum - c[k]; i >= 0; i--){
            check[i + c[k]] |= check[i];
        }
    }

    for(int i = 1; i <= sum; i++){
        std::cout << i << " " << check[i]<< std::endl;
    }
    delete[] check;
}
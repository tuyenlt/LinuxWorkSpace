#include <bits/stdc++.h>
#include <fstream>

#define IMG_WIDTH 600
#define IMG_HEIGHT 800

using namespace std;
bool checked[IMG_HEIGHT][IMG_WIDTH] = {0};
int m_i[] = {1, 1,0, 0,1,-1,-1,-1};
int m_j[] = {1,-1,1,-1,0 ,0, -1,1};
int max_x = 0;
int max_y = 0;
int min_x = IMG_WIDTH;
int min_y = IMG_HEIGHT;


void BFS(char (*img)[IMG_WIDTH],int i,int j){
    checked[i][j] = true;
    for(int k = 0; k<8;k++){
        int x = j + m_j[k];
        int y = i + m_i[k];
        if(x < 0 || y < 0 || x > IMG_WIDTH || y > IMG_HEIGHT || img[y][x] == 32 || img[y][x] == 0){
            if(j > max_x)max_x = j;
            if(j < min_x)min_x = j;
            if(i < min_y)min_y = i;
            if(i > max_y)max_y = i;
        }
        else if(!checked[y][x])BFS(img,y,x);
    }
}



int main(){
    char img[IMG_HEIGHT][IMG_WIDTH] = {0};
    string temp;
    int line = 0;
    for(int i=0;i<17;i++){
        getline(cin,temp);
        for(int j=0;j<temp.length();j++){
            img[i][j] = temp[j];
        }

    }
    int done = 0;
    for(int i=1;i<IMG_HEIGHT;i++){
        for(int j=0;j<IMG_WIDTH;j++){
            if(img[i][j] != 32){
                BFS(img,i,j);
                done = 1;
                break;
            }
        }
        if(done)break;
    }
    for(int i=0;i<40;i++){
        for(int j=0;j<40;j++){
            cout << checked[i][j];
        }
        cout << endl;
    }
    cout << min_x << " " << min_y << endl;
    cout << max_x << " " << max_y << endl;
    return 0;
}
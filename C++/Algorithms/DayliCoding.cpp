#include <iostream>
#include <cstdlib>
#include <unordered_map>
#include <map>
#include <algorithm>

using namespace std;

int random(int a, int b){
    return a + rand() % (b - a + 1);
}

void SecondMaxReNum(){
    int n,input;
    cin >> n;
    unordered_map<int,int> map;
    for(int i=0;i<n;i++){
        cin >> input;
        map[input]++;
    }
    int max1 = map.begin() -> first;
    int max2 = max1;
    for(unordered_map<int,int> :: iterator it = map.begin(); it!=map.end();it++){
        if(it -> second > map[max1]){
            max2 = max1;
            max1 = it -> first;
        }
    }
    cout << max2;
}
//...............................
struct MAXVAL{
    int val;
    bool found = false;
};

int a[101][101];
MAXVAL maxPath[100][100];

int maxPoint(int n,int i,int j){
    int res;
    if(maxPath[i][j].found == false){
        if(j == n) res = a[i][j];
        else if(i == 0) res = a[i][j] + max(maxPoint(n,i,j++),maxPoint(n,i++,j++));
        else if(i == n) res = a[i][j] + max(maxPoint(n,i,j++),maxPoint(n,i--,j++));
        else res = a[i][j] + max(maxPoint(n,i++,j++), max(maxPoint(n,i,j++),maxPoint(n,i--,j++)));
        maxPath[i][j].val = res;
        maxPath[i][j].found = true;
        return res;

    }else return maxPath[i][j].val; 
}


void MaximumPath(){
    int n;
    cin >> n;
    for(int i = 1; i<n+1; i++){
        for(int j = 1; j<n+1;j++){
            cin >> a[i][j];
        }
    }
    //......................
    int res = INT8_MIN;
    int temp;
    for(int i = 0; i<n+1;i++){
        temp = maxPoint(n,i,1);
        if(temp > res) res = temp;
    }   
    cout << temp;
}
//..........................................................


bool DragonFight(int MyPower,multimap<int,int> Dra){
    for(multimap<int,int> :: iterator it = Dra.begin(); it != Dra.end(); it++){
        if(MyPower > it-> first) MyPower += it -> second;
        else return false;
    }
    return true;    
}




int main(){
    double in = 0;
    double out = 0;
    int test = 100000;
    for(int i =0;i<test;i++){
        int x = random(0,100);
        int y = random(0,100);
        if(x*x + y*y >= 100*100) out ++;
        else in++;
    }
    cout << in << " " << out << endl;
    double pi = (in/(in+out))*4;
    cout << pi;
    return 0;
}
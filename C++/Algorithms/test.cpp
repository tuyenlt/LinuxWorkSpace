#include <bits/stdc++.h>

using namespace std;

int solution(int p[],int s[],int n){
    vector<int> month_amount[13];
    int amount = 0;
    int fee = 5*12;
    for(int i=0;i<n;i++){
        string month = date[i].substr(5,2);
        int index = stoi(month);
        month_amount[index].push_back(a[i]);
        amount += a[i];
    }
    for(int i=1;i<13;i++){
        int cnt = 0;
        int card_money = 0;
        for(int j : month_amount[i]){
            if(j < 0) card_money += j;
        }
        if(cnt >= 3 && card_money <= -100)fee -= 5;
        
    }
    return amount - fee;
}


int main(){
    
    return 0;
}
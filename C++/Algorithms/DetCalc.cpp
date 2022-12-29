#include <iostream>
#include <fstream>

using namespace std;

// maximum det size 100

// class INT_MATRIX{
//     int*** mat;
//     int num_rows = 0;
//     int num_cols = 0;
// public: 
//     INT_MATRIX(int rows, int cols){
//         num_cols = cols;
//         num_rows = rows
//         int*** new_mat = new (int**)[rows];
//     }

// };

void showDet(float det[100][100],int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout << det[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

double detCalc(float det[100][100],int size){
    double res =1;
    for(int i = 1; i<size; i++){
        for(int j=i;j<size;j++){
            float arg = det[j][i-1] / det[i-1][i-1];
            det[j][i-1] = 0;
            for(int n=i;n<size;n++){
                det[j][n] = det[i-1][n]*arg - det[j][n];
            }
        }
        showDet(det,size);
    }
    for(int i=0;i<size;i++)res*=det[i][i];
    return res;
}

int main(){
    fstream data("det_data.txt");
    float det[100][100];
    for(int i=0;i<5;i++){
        for(int j=0;j<4;j++){
            data >> det[i][j];
        }
    }
    cout << detCalc(det,5);
    return 1;
}
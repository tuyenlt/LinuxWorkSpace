#include "input.h"
#include <iostream>

int* array_input(int n){
    int *a = new int(n);
    for(int i=0;i<n;i++) std::cin >> a[i];
    return a;
}
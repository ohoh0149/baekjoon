// Online C++ compiler to run C++ program online
#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int n,m,a,b,c;
    cin>>n>>m;
    int arr[101];
    for(int i=0;i<101;i++){
        arr[i]=0;
    }
    for(int i=0;i<m;i++){
        cin>>a>>b>>c;
        
        for(int j=a;j<b+1;j++){
            arr[j]=c;
        }
        
    }
    for(int i=1;i<n+1;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}
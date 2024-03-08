#include <iostream>
#include <string>
using namespace std;

int main(){
    int n,p;
    cin>>n;
    for (int t = 0; t < n; t++)
    {
        cin>>p;
        int max=0,c=0;
        string name;
        string result;
        for (int i = 0; i < p; i++)
        {
            cin>>c>>name;
            if(c>max){
                max=c;
                result=name;
            }
        }
        cout<<result<<endl;
        
    }
    
    return 0;

}
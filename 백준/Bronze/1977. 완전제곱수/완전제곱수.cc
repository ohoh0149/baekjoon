#include <iostream>

using namespace std;

int main(){
    int m;
    int n;
    cin>>m;
    cin>>n;
    int sm=0;
    int min=10001;
    bool flag=false;
    for (int i = m; i <=n ; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            
            if (j*j==i)
            {
                if(! flag){
                    flag=true;
                    min=i;
                }
                sm+=i;
                break;
            }
            
        }
        
    }
    if( min ==10001)
    {
        cout<<-1<<endl;
    }
    else{
    cout<<sm<<endl;
    cout<<min<<endl;
}
    return 0;

}
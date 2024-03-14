
#include <iostream>

#include <algorithm>
using namespace std;
int main()
{
    int a,b,c;
    int score=0;
    cin>>a>>b>>c;
    if(a==b&& b==c){
        score=10000+a*1000;
    }
    else if(a==b &&b!=c){
        score=1000+a*100;
    }
    else if(c==b &&a!=c){
        score=1000+b*100;
    }
    else if(a==c &&b!=a){
        score=1000+a*100;
    }
    else{
        score=max(max(a,b),c)*100;
        
    }
    cout<<score;
    return 0;
}

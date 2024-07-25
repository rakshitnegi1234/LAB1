#include<iostream>
#include<string>
using namespace std;
int main()
{
    string s;
    cin>>s;
    cout<<"old string: "<<s<<endl;
    int n=s.size();
    int i=0,j=n-1;
    while(i<j)
    {
        swap(s[i],s[j]);
        i++;
        j--;
    }
    cout<<"new string "<<s;
    return 0;
}

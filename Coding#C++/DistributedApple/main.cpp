#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t!=0){
	    int n,k;
	    cin>>n>>k;
	    int result = n/k;
	    int r[k];
	    fill(r,r+k,0);
	    int i = 0 ;
	    int flag = 1;
	    while(n!=0){
            r[i] += k;
            n -= k;
            if(r[i]>result){
                flag = 2;
                cout<<"YES\n";
                break;
            }
            i = (i+1)%k;
	    }
	    if(flag == 1){
            cout<<"NO\n";
	    }
	}
	return 0;
}

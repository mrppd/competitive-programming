#include "iostream"
#include "numeric"
using namespace std;


int isGood(long long int a[], long long int n){
    long long int tmp_a;
    for(int i=0; i<n; i++){
        tmp_a = a[i];
        a[i] = 0;
        if(accumulate(a, a+n, 0)==tmp_a){
            //cout<<"y "<<arraySum(a, i)<<endl;
            a[i] = tmp_a;
            return 1;
        }
        a[i] = tmp_a;
    }

    return 0;
}

int main(){

    long long int tcase, n, a[200005], res;

    cin>>tcase;
    while(tcase){

        cin>>n;
        for(int i=0; i<n; i++){
            cin>>a[i];
        }

        long long int cnt = 0;
        for(int i=0; i<n; i++){
            if(isGood(a, i+1)){
                cnt++;
                //cout<<res<<' '<<i<<endl;
            }
        }

        printf("%d\n", cnt);


        tcase--;
    }
    return 0;
}

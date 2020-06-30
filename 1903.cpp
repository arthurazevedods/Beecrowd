#include <iostream>
#include <vector>


using namespace std;

int main(){
    int M, N,U,V,count1=0,count2=0;
    bool bolada = true;
    cin >> M >> N;

    vector<int> st(M + 1, 0);
    vector<int> dest(M + 1, 0);

    for (int i = 0; i < N; i++){
        cin >> U >> V;
        st[U]++;
        dest[V]++;
      
    }

    
    int out = 0, in = 0;
    for (int i = 1; i <= M; i++){
        if (st[i] == 0)
            in++;
        if (dest[i] == 0)
            out++;

        if (out > 1 || in > 1)
        {
            bolada = false;
            break;
        }
    }

    if(bolada){
        cout << "Bolada" << endl;
    }
    else{
        cout << "Nao Bolada" << endl;
    }

    return 0;
}
/* Problem link:
https://neps.academy/br/exercise/5
*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int H, P, F, D;

    cin >> H >> P >> F >> D;

    while(true) {
        F += D;
        if (F == -1)
            F = 15;
        if (F == 16)
            F = 0;
        if (F == P) {
            cout << "N" << endl;
            return 0;
        }
        if (F == H) {
            cout << "S" << endl;
            return 0;
        }
    } 
    return 0;
}
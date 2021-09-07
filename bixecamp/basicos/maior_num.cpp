/* Problem link:
https://neps.academy/br/exercise/323
*/
#include <bits/stdc++.h>
using namespace std;

int main(){
    int num = 1, max = -1;

    while (num != 0) {
        cin >> num;
        if (num > max)
            max = num;
    }
    cout << max << endl;

    return 0;
}
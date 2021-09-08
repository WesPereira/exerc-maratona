/* Problem link:
https://neps.academy/br/exercise/52
*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, a = 0, b = 0, num;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> num;

        if (num == 1)
            a = (a + 1) % 2;
        else {
            a = (a + 1) % 2;
            b = (b + 1) % 2;
        }
    }
    cout << a << endl;
    cout << b << endl;
    
    return 0;
}
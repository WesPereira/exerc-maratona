/* Problem link:
https://codeforces.com/problemset/problem/110/A
*/
#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

int main() {
    LL num;
    int count = 0;

    cin >> num;

    while (num > 0) {
        int digit = num % 10;
        if (digit == 4 || digit == 7)
            count++;
        num /= 10;
    }

    if (count == 4 || count == 7)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;

    return 0;
}
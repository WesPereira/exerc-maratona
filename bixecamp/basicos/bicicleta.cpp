/* Problem link:
https://codeforces.com/contest/659/problem/D
*/
#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, x, y, xant, yant, true_diff_x, true_diff_y, count=0, ordem = 0, resp = 0;

    cin >> n >> xant >> yant;

    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        int diffx = x - xant;
        int diffy = y - yant;
        if (diffx != 0) {
            true_diff_x = diffx;
            count++;
            ordem = 2;
        }
        if (diffy != 0) {
            true_diff_y = diffy;
            count++;
            ordem = 1;
        }
        if (count == 2) {
            count--;
            if ((true_diff_x > 0 && true_diff_y > 0 && ordem == 1) ||
                (true_diff_x > 0 && true_diff_y < 0 && ordem == 2) ||
                (true_diff_x < 0 && true_diff_y < 0 && ordem == 1) ||
                (true_diff_x < 0 && true_diff_y > 0 && ordem == 2))
                resp++;
        }
        xant = x;
        yant = y;
    }
    cout << resp << endl;

    return 0;
}
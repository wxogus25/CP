#include <bits/stdc++.h>

using namespace std;

int uni[51];
vector<vector<int> > e;

int f(int now) {
    if (now == uni[now] || uni[now] == -1)
        return now;
    else
        return uni[now] = f(uni[now]);
}

int u(int a, int b) {
    if (uni[a] < uni[b])
        return uni[b] = uni[a];
    else
        return uni[a] = uni[b];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, m, t;
    cin >> n >> m;

    cin >> t;
    for (int i = 1; i <= n; i++) uni[i] = i;
    for (int i = 0; i < t; i++) {
        int c;
        cin >> c;
        uni[c] = -1;
    }
    e.resize(m);
    for (int i = 0; i < m; i++) {
        cin >> t;
        int a, b;
        cin >> a;
        e[i].push_back(a);
        for (int j = 1; j < t; j++) {
            cin >> b;
            e[i].push_back(b);
            a = u(f(a), f(b));
        }
    }
    int dap = m;
    for (int i = 0; i < m; i++) {
        for (auto &&j : e[i]) {
            if (uni[f(j)] == -1) {
                dap--;
                break;
            }
        }
    }
    cout << dap;
}
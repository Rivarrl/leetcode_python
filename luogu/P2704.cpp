#include <iostream>
#include <cstdio>
#include <cstring>
#define MAXSTATE 70 // 单行最多100个位置时的行内满足条件的状态最大估计值
#define MAXROW 101
#define MAXCOL 11
#define max(a,b) a>b?a:b
#define mset(a) memset(a,0,sizeof(a))
using namespace std;

int n, m;
int arr[MAXROW]; // 记录地形，平地：0，山坡：1
int sta[MAXSTATE]; // 记录行内满足条件的状态, 摆放炮兵：1，不摆放：0
int count[MAXSTATE]; //记录每种状态对应的1的个数
int dp[MAXROW][MAXSTATE][MAXSTATE]; // dp[i][j][k]表示第i行为状态j且第i-1行为k时的最优解
char ch;
int main() {
    mset(arr), mset(sta), mset(count), mset(dp);
    cin >> n >> m;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            cin >> ch;
            // 山坡不能摆放炮兵，相当于已经摆放的状态：1
            if (ch == 'H') { 
                arr[i] |= (1 << j);
            }
        }
    }
    int c = 0;
    // 预处理，把所有一行内符合条件的布阵状态记录到sta，对于的1的个数记录到count
    for (int i=0; i<(1<<m); i++) {
        if ((i & (i << 1)) || (i & (i << 2))) continue;
        int k = i;
        while (k > 0) {
            count[c] += (k & 1);
            k >>= 1;
        }
        sta[c++] = i;
    }
    // 初始化第1行
    for (int i=0; i<c; i++) {
        if (sta[i] & arr[0]) continue;
        dp[0][i][0] = count[i];
    }
    // 初始化第2行
    for (int i=0; i<c; i++) {
        if (sta[i] & arr[1]) continue;
        for (int j=0; j<c; j++) {
            if (sta[j] & arr[0]) continue;
            if (sta[i] & sta[j]) continue;
            dp[1][i][j] = max(dp[1][i][j], dp[0][j][0] + count[i]);
        }
    }
    // 从第3行开始dp
    for (int i=2; i<n; i++) {
        for (int j=0; j<c; j++) {
            // 炮兵不能上山
            if (sta[j] & arr[i]) continue;
            for (int k=0; k<c; k++) {
                if (sta[k] & arr[i-1]) continue;
                // 两行的炮兵互相伤害
                if (sta[j] & sta[k]) continue;
                for (int p=0; p<c; p++) {
                    if (sta[p] & arr[i-2]) continue;
                    if ((sta[j] & sta[p]) || (sta[k] & sta[p])) continue;
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][k][p] + count[j]);
                }
            }
        }
    }
    int res = 0;
    for (int i=0; i<c; i++) {
        for (int j=0; j<c; j++) {
            res = max(res, dp[n-1][i][j]);
        }
    }
    cout << res;
    return 0;
}
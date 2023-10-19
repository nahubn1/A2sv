#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph;
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph.push_back({u - 1, v - 1, w});
    }

    vector<int> dist(n, 30000);
    dist[0] = 0;

    for (int i = 0; i < n - 1; i++) {
        for (const auto& edge : graph) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];

            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
            }
        }
    }

    for (int d : dist) {
        cout << d << " ";
    }

    return 0;
}

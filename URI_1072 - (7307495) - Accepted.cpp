#include <bits/stdc++.h>
using namespace std;

int main() {

	int in = 0, out = 0, c, n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> c;
		if (10 <= c && c <= 20)
			in++;
		else
			out++;
	}
	cout << in<<" in"<<endl;
	cout<<out<<" out"<<endl;



}

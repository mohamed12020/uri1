#include <bits/stdc++.h>
using namespace std;

int main() {
	int num;
	int max = 0;
	int pos = 0;
	for (int i = 0; i < 100; ++i) {
		cin >> num;
		if (num > max){
			max = num;
		    pos = i;
		}

	}
	 cout << max << "\n" << pos+1 << "\n";
}


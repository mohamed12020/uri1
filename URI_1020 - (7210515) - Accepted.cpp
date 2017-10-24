#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
	int d,NYear,NMouns,NDay;
	cin>>d;
	NYear=int(d/365);
	NMouns=int((d%365)/30);
	NDay=((d%365)%30);
	cout<<NYear<<" ano(s)" <<endl;
	cout<<NMouns<<" mes(es)"<<endl;
	cout<<NDay<<" dia(s)"<<endl;
}

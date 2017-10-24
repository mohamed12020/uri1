#include <iomanip>      //
#include <iostream>
using namespace std;

int main() {
	double r,b=3.14159,total;
	cin>>r;
	total=r*r*b;
	cout<<fixed<<setprecision(4)<<"A="<<total<<endl;
}

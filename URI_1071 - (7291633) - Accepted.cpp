#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {

int a,b,sum;
sum=0;
cin>>a>>b;
if(a<b)
{
	for (int i=a+1;i<b;i++)
	{
		if (i%2!=0)
			sum+=i;

	}
}
if(a>b)
{
  for (int i=b+1; i<a; i++)
	{
		if (i%2!=0)
		 sum+=i;
	}
}
cout<<sum<<endl;
}

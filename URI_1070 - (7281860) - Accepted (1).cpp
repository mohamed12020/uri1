#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
	int num,count;
	cin>>num;
	count=0;
	if (num%2==0)
	{
	  for (int i=num+1;i<100;i+=2)
	  {
	      cout<<i<<endl;
	      count+=1;
	      if (count==6)
	        	break;
		}

	  }
	else if (num%2!=0)
		 for (int i=num+2;i<100;i+=2)
		 {
		 cout<<i<<endl;
		 count+=1;
         if (count==6)
        	break;
	}


}

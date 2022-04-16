#include<stdio.h>

int main(int arr, char* args[])
{
	char *s;
	int j, x=0;
	char str[100] ={'f','i','r','e','f','o','x',' ','-','s','e','a','r','c','h'} ;
	x = 17;
	str[x-2] = ' ';
	str[x-1] ='"';
	for(int i = 1; i<arr; i++)
	{
		s = args[i];
		j = 0;
		while(s[j] != '\0')
		{
			str[x] = s[j];
			x++;
			j++;
		}
		str[x] = ' '; x++;
	}
	str[x-1] = '"';
	str[x] = ' ';
	str[x+1] = '&';
	str[x+2] = '\0';
	system(str);
	return 0;


}

#include<stdio.h>

int main()
{
    int a=1,b=1;
    while(scanf("%d%d",&a,&b) != EOF)
    {
		printf("%d\n",a+b);
    }
    return 0;
}
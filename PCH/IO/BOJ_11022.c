#include <stdio.h>

int main(void)
{
    int a,i;
    scanf("%d", &a);
    for(i=1; i<a+1; i++)
    {
    	int x,y;
    	scanf("%d%d",&x,&y);
    	
        printf("Case #%d: %d + %d = %d\n",i,x,y ,x+y);
    }
    return 0;
}
#include<stdio.h>
#define toggle(x) (x = !x)
 
int main()
{
    int light_on[3][3];
 
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            int n;
            scanf("%d",&n);
 
            if(n%2 == 1)
            {
                toggle(light_on[i][j]);
                if(j!=0)
                toggle(light_on[i][j - 1]);
                if(j!=2)
                toggle(light_on[i][j + 1]);
                if(i!=2)
                toggle(light_on[i + 1][j]);
                if(i!=0)
                toggle(light_on[i - 1][j]);
            }
        }
    }
 
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            if(light_on[i][j])
                printf("1");
            else
                printf("0");
        }
        printf("\n");
    }
    return 0;
}
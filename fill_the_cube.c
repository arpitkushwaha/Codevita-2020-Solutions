#include <stdio.h>
#include<math.h> 
#include <stdlib.h>

int main() {
	int n,count=0,i,j,r;
    char arr[100][100];
    float s=0; 
    scanf("%d\n", &n); 
    for(i=0;i<n;i++) 
    { 
        for(j=0;j<n;j++) 
        {
      
            if(i==n-1 && j==n-1)
            	break;
            if(j==n-1)
            	scanf("%c", &arr[i][j]);
            else
				scanf("%c ", &arr[i][j]); 
        }
    } 
    for(i=0;i<n;i++) 
    {
        for(j=0;j<n;j++) 
        { 
            if(arr[i][j]=='D') 
                count=count+1; 
        }
    } 
        s=sqrt(count); 
        r=floor(s); 
        printf("%d",r); 
            
        return 0;
}
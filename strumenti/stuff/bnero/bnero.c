#include <stdio.h>
#define MAXN   1000
char coll[MAXN]; int n, i;

void scrivi() {
    for (i=0;i<n;i++)
        printf("%c",coll[i]);
    printf("\n");
}


int main() {
    FILE *fr = fopen( "input.txt", "r" );
	FILE *fw = fopen( "output.txt", "w" );
    fscanf(fr,"%d",&n);
    for (i=0;i<n;i++) do {
        fscanf(fr,"%c",&coll[i]);
    } while( (coll[i] != 'N') && (coll[i] != 'B') );
    fclose(fr);
    int left = 0;
    int right = n-1;
    while( coll[right] == coll[left] ) {
      right--;
      if(right < 0) {
         fclose(fw);
         return 0;
      }
    }
    while( coll[right-1] == coll[right] ) right--;
    while( coll[left+1] == coll[left] ) left++;
//    NNNNNNNNB .......     NBBBBBBBNNN
//           ^               ^
//           left            right
//NBNNBNBBN
//012345678
//  ^      ^
    while(left+1 < right-1) {
       for (i=0;i<n;i++) printf("%d",i); printf("\n");
       //scrivi();
       //for (i=0;i<n;i++) printf( "%c", ( (i==left) || (i==right))?'^':' '); printf("\n");
       fprintf(fw,"%d %d\n", left+1, right-1);
       printf("%d %d\n", left+1, right-1);
       getchar();
       left++; right--;
       while( coll[right-1] == coll[right] ) right--;
       while( coll[left+1] == coll[left] ) left++;       
    }
    fclose(fw);
    return 0;
}



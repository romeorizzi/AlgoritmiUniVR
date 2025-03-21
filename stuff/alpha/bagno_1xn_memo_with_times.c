#include<stdio.h>
#include<assert.h>

#define MAXN 10000000
#define UNKNOWN -1

int memo[MAXN +1];
int closed[MAXN +1], time = 0;

int numPiastrellature(int n) {
  assert( n >= 0 );
  if( memo[n] != UNKNOWN ) return memo[n];
  memo[n] = numPiastrellature(n-2) + numPiastrellature(n-1) % 1000000;
  closed[n] = time++;
  return memo[n];
}

int main() {

  int n, i;
   scanf("%d", &n);

   for(i = 0; i <= MAXN; i++)
     memo[i] = UNKNOWN;

   memo[0] = memo[1] = 1;
   closed[0] = closed[1] = time++;

   printf("%d\n", numPiastrellature(n) );

   for(i = 0; i <= n; i++) {
     printf("%d\t", i );
   }
   printf("\n");
   for(i = 0; i <= n; i++) {
     printf("%d\t", memo[i] );
   }
   printf("\n");
   for(i = 0; i <= n; i++) {
     printf("%d\t", closed[i] );
   }

   return 0;
}

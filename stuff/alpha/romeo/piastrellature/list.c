#include<stdio.h>
#include<assert.h>

#define MAX_N 100
char prefix[MAX_N];

void printSol(int pos_write) {
  {int i; for(i = 0; i < pos_write; i++)
	    printf("%c", prefix[i]);
  }
  printf("\n");
}


void listaPiastrellature(int n, int pos_write) {
/*
   assume che in prefix[0, ..., pos_write-1 ] sia presente
   un prefisso di piastrellatura possibile e che rimanga ancora
   da coprire un bagno residuo di lunghezza n. 
*/
  assert( n >= 0 );
  if(n==0) { printSol(pos_write); return; }
  prefix[pos_write] = '1';
  listaPiastrellature(n-1, pos_write +1);
  if(n>=2) {
     prefix[pos_write] = '2';
     listaPiastrellature(n-2, pos_write +1);
  } 
}

int main() {
  printf("Inserire numero piastrelle: ");
  int n; scanf("%d", &n); assert( n <= MAX_N );
  listaPiastrellature(n, 0);
}

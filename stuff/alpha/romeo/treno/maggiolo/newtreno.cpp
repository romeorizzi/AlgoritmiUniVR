/*
 Stefano Maggiolo
*/

#include <iostream>
#include <fstream>

#define EVAL

using namespace std;

const int MAXN = 1000;
int N, vuoto;
char treno[2*MAXN+3];

#if !defined(EVAL)
  istream &in(cin);
  ostream &out(cout);
#else
  ifstream in("input.txt");
  ofstream out("output.txt");
#endif

void initTreno() {
  vuoto = 2*N+1;  
  for(int i = 1; i <= N; i++)  { treno[i] = 'A'; treno[i+N] = 'B'; }
  treno[2*N+1] =  treno[2*N+2] =  'X';
}

void printTreno() {
  for(int i = 1; i <= 2*N+2; i++)  { cout << treno[i]; }
  cout << endl;
  for(int i = 1; i <= 2*N+2; i++)  { out << treno[i]; }
  out << endl;
}


void o(int x) {
  //cout << x+1 << " " << vuoto << endl;
  treno[vuoto] = treno[x+1]; treno[vuoto+1] = treno[x+2];
  treno[x+1] = treno[x+2] = 'X';
  vuoto = x+1;
  printTreno();
}

int
main(void)
{
  in >> N;
  
  int t = N % 4;
  int M = (N-t)/4;

  initTreno();
  printTreno();
  if (N == 3)
    {
      o(1);
      o(5);
      o(3);
      o(6);
    }
  else if (N == 4)
    {
      o(3);
      o(1);
      o(5);
      o(2);
      o(8);      
    }
  else if (N % 2 == 0)
    {
      o(3-t);
      o(2*N-3);
      o(2*N-1);
      for (int i = 1; i < M-1+t/2; i++)
        {
          o(N-2+4*i);
          o((3-t)+4*i);
        }
      o(2*N-6 + t/2);

      for (int i = 0; i < M; i++)
        {
          o(t+4*i);
          o(N-1+4*i);
        }
      o(2*N);
    }
  else if (N % 4 == 1)
    {
      o(2);
      o(2*N-3);
      o(2*N-1);
      for (int i = 1; i < M; i++)
        {
          o(N-2+4*i);
          o(2+4*i);
        }
      o(2*N-4);

      for (int i = 0; i < M-1; i++)
        {
          o(1+4*i);
          o(N+1+4*i);
        }
      o(N-4);
      o(2*N);
    }
  else if (N % 4 == 3)
    {
      o(1);
      o(2*N-3);
      o(2*N-1);
      for (int i = 1; i <= M; i++)
        {
          o(N-3+4*i);
          o(1+4*i);
        }

      for (int i = 0; i < M; i++)
        {
          o(2+4*i);
          o(N+2+4*i);
        }
      o(2*N);
    }
  system("PAUSE");
  return 0;
}
  

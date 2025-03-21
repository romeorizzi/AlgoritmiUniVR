/* FILE: intervalloSommaMassima.cpp   last change: 6-March-2012   author: Romeo Rizzi
 */

// #include <iostream> // NOTA: ho commentato questa riga per essere sicuro di non aver lasciato operazioni di input/output di debug nella fretta di consegnare, se compila cosi' non ci sono ed io non perdo stupidamente i miei punti-esame.
#include <cstdlib>
#include <fstream>
#include <cassert>

using namespace std;

const int MAX_N = 1000000;
int n, vect[MAX_N], prefixSum[MAX_N +1];

int main() {
  ifstream fin("input.txt"); assert(fin);
  fin >> n;
  prefixSum[0] = 0;
  for(int i = 0; i < n; i++) {
    fin >> vect[i];
    prefixSum[i+1] = prefixSum[i] + vect[i]; 
  }
  fin.close();

  int max_so_far = vect[0];
  for(int len = 1; len < n; len++)
    for(int start = 0; start + len <= n; start++) {
      int somma = prefixSum[start + len] - prefixSum[start];
      if( somma > max_so_far ) max_so_far = somma;
    }

  ofstream fout("output.txt"); assert(fout);
  fout << max_so_far << endl;
  fout.close();
  return 0;
}

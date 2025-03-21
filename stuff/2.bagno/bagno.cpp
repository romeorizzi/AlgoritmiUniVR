/* FILE: bagno.cpp   last change: 12-March-2012   author: Romeo Rizzi
 */

#include <iostream> // NOTA: ho commentato questa riga per essere sicuro di non aver lasciato operazioni di input/output di debug nella fretta di consegnare, se compila cosi' non ci sono ed io non perdo stupidamente i miei punti-esame.
#include <cstdlib>
#include <fstream>
#include <cassert>

using namespace std;

long long int numPiastrellature(int n) {
// ritorna il numero di modi di piastrellare un bagno 1xn con piastrelle 1x1 e 1x2  (il numero va ritornato modulo 1000000007)
  assert ( n >= 0 );
  if( n <= 1 ) return 1;
  return ( numPiastrellature(n-1) + numPiastrellature(n -2) ) % 1000000007;
}



int main() {
  ifstream fin("input.txt"); assert(fin);
  int n; fin >> n;
  fin.close();

  ofstream fout("output.txt"); assert(fout);
  fout << numPiastrellature(n) << endl;
  fout.close();
  return 0;
}

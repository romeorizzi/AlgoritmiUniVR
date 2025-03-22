#include <iostream>
#include <assert.h>


using namespace std;

/**
 * Treno:
 * AAABBB**
 * 12345678
 */

const int N = 12;
const int L = 2*N +2;

char treno [L +1]; int pos_XX;
int moves[2*N];

// 2*N - 1, se chiamiamo init_best_sol(0,0)
int upperBound = N+2;
int best_sol[2*N];
void init_best_sol (int n, int pos_write) {
    assert ( n >= 2);
	if (n==3) {
		best_sol[pos_write++] = 2;
		best_sol[pos_write++] = 6;
		best_sol[pos_write++] = 4;
		best_sol[pos_write++] = 7;
	} else {  assert ( n > 3 );
		best_sol[pos_write++] = n;
		best_sol[pos_write++] = 2*n-1;
		init_best_sol(n-1, pos_write);
		if (pos_write == 2)	best_sol[upperBound-1] = 2*n+1;
	}
}

int lowerBound(int n) {
	int numAB = 0;
	int numBA = 0;
	for (int i = 1; i < L; i++) {
		if (treno[i] == 'A' && treno[i+1] == 'B')
			numAB++;
		if (treno[i] == 'B' && treno[i+1] == 'A')
			numBA++;
	}
	return (2*n-1-numAB-numBA)/2+(((2*n-1-numAB-numBA)%2)?1:0);
}


void initTreno () {
	for (int i = 1; i <= N; i++)
		{ treno[i] = 'A'; treno[i+N] = 'B'; }
	treno[2*N+1] = '*'; treno[2*N+2] = '*'; pos_XX = 2*N+1; 
}
	

void stampaTreno() {
	for (int i = 1; i <= L; i++)
		cout << treno[i];
	cout << endl;
}

void stampaBestSol () {
	cout << "numero mosse ottimo = " << upperBound << endl;
	for (int i = 0; i < upperBound; i++)
		cout << best_sol[i] << " ";
	cout << endl;
}

/**
 * Sposta gli '*' alle posizioni i e i+1, utilizzando la numerazione partendo dal 1.
 * Se la mossa non possibile si blocca.
 */
void spostamento(int i) {
	assert(i > 0);
	assert(i+1 <= L);
	assert(treno[i] != '*' && treno[i+1] != '*');

    treno[pos_XX] = treno[i]; treno[pos_XX+1] = treno[i+1];
    treno[i] = treno[i+1] = '*';
    pos_XX = i;
}

/**
 * Controlla se il treno Ã¨ giÃ  risolto.
 */
bool giaRisolto () {
	for (int i = 1; i <= 2*N; i++) {
		if (i % 2) {
			if (treno[i] != 'A')
				return false;
		} else {
			if (treno[i] != 'B')
				return false;
		}
	}
	if (treno[L] != '*' || treno[L-1] != '*')
		return false;
	return true;
}


bool verifyBestSol() {
    cout << " Verifying bestSol ..." << endl;
	initTreno(); stampaTreno();
	for (int i = 0; i < upperBound; i++) {
		spostamento(best_sol[i]);
		stampaTreno();
	}	
	return giaRisolto();
}

void tryAll (int step) {
	if (step+lowerBound(N) >= upperBound ) 	return;

    if (giaRisolto()) {
       cout << "Improvement found ! " << step << endl;
       upperBound = step;
       for (int i = 0; i < step; i++)
       	  best_sol[i] = moves[i];
       return;
    }
	
	// provare tutte le possibili mosse
	int mem_pos_XX = pos_XX;
	for (int i = 1; i < L; i++) {
	   if( (i != pos_XX) && (i != pos_XX +1 ) && (i != pos_XX -1) ) {
          moves[step] = i;
	      spostamento(i);
		  tryAll (step +1);
	      spostamento(mem_pos_XX);
	   }
	}
}

int main (void) {
	//init_best_sol(N,0);
	//stampaBestSol();
	//assert(verifyBestSol());

	initTreno();
	tryAll(0);
	stampaBestSol ();
	assert(verifyBestSol());
	
	return 0;
}

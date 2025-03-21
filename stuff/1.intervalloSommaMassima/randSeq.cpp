/* FILE: randSeq.cpp   last change: 6-March-2013   author: Romeo Rizzi
 * This program generates a sequence of n random integers.
 * Usage syntax:
 *   > randSeq out_file n MIN_MAV MAX_VAL seed
 */

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

using namespace std;

int RandNumber(int min, int max) {
  /* returns an integer in [min, max]
   * see Stroustrup "The c++ Programming Language" 3th edition pg. 685
   * for comments on the following manipulation choice.
   * In particular, considerations on the bad quality of low bits come into account.
   */
 return min + (int) ( (max-min) * (double(rand()) / RAND_MAX) );
}



int main(int argc, char** argv) {
  srand(time(NULL));
  int n, MIN_VAL = -100, MAX_VAL = 90;
  n = atoi(argv[2]);
  if(argc > 3) MIN_VAL = atoi(argv[3]);
  if(argc > 4) MAX_VAL = atoi(argv[4]);
  if(argc > 5) srand( atoi(argv[5]) );

  ofstream fout(argv[1]);
  fout << n << endl;
  for(int i = 1; i <= n; i++)
    fout <<  RandNumber(MIN_VAL, MAX_VAL) << " ";
  fout << endl;
  fout.close();
  return 0;
}

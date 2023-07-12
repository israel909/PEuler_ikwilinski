#include <iostream>
#include <vector>
#include <string>
#include <queue>

#define TWO_HUNDRED "200"

using namespace std;

vector<long long int> genPrimes(long long int limit) {
  vector<long long int> primes;
  bool* primeSieve = new bool[limit - 2];
  for (long long int i = 0; i < limit - 2; i++)
    primeSieve[i] = false;
  long long int startIndex = 0;
  while (startIndex < limit - 2) {
    if (!primeSieve[startIndex]) {
      long long int prime = startIndex + 2;
      primes.push_back(prime);
      for (long long int i = startIndex + prime; i < limit - 2; i += prime) {
        primeSieve[i] = true;
      }
    }
    if (primes.size() < 10)
      startIndex++;
    else
      startIndex += 2;
  }
  delete [] primeSieve;
  return primes;
}

// bool isPrimeProof(string num)


int main() {
    int LIMIT = 1000;
    vector<long long int> primes = genPrimes(LIMIT + 1);
    vector<string> squbes;
    
    priority_queue<string> pq;



    return 0;
}
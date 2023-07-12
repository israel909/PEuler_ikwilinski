#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <assert.h>
#include <chrono>

#define TEST_LIMIT 1000000

using namespace std;

unsigned long long findMin(const unsigned int p, const unsigned int q) {
    const string s = to_string(p);
    for (int i = 1; i <= TEST_LIMIT; i++) {
        unsigned long long testNum = stoull(to_string(i) + s);
        if (testNum % q == 0) {
            return testNum;
        }
    }
    return 0;
}


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

int main(int argc, char* argv[]) {
    bool verbose = argc == 2 && (string(argv[1]) == "-v" || string(argv[1]) == "--verbose"); // verbose mode
    int LIMIT = 1000000;
    vector<long long int> primes = genPrimes(LIMIT + 1);
    primes.erase(primes.begin());
    primes.erase(primes.begin());
    unsigned long long sum = 0;
    
    // Start timer
    auto start = chrono::high_resolution_clock::now();
    for (int i = 0; i < primes.size() - 1; i++) {
        unsigned long long res = findMin(primes[i], primes[i + 1]);
        assert(res != 0);
        sum += res;
        if (verbose)
            cout << primes[i] << " " << primes[i + 1] << " " << res << " " << sum << "\n";
    }
    // End timer
    auto end = chrono::high_resolution_clock::now();
    cout << "Answer: " << sum << "\n";
    cout << "Time: " << chrono::duration_cast<chrono::milliseconds>(end - start).count() << " ms\n";
    return 0;
}
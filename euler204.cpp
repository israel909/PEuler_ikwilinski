#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <vector>
#include <chrono>

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


long long int countHammingNumbers(int type, long long int LIMIT) {
  vector<long long int> primes = genPrimes(type + 1);
  long long int total = 1;
  queue<long long int> nums;
  unordered_set<long long int> visited;

  for (int i = 0; i < primes.size(); i++) {
    nums.push(primes[i]);
    visited.insert(primes[i]);
  }

  while (!nums.empty()) {
    long long int num = nums.front();
    total++;
    nums.pop();
    for (int i = 0; i < primes.size(); i++) {
      long long int newNum = num * primes[i];
      if (newNum <= LIMIT && visited.find(newNum) == visited.end()) {
        nums.push(newNum);
        visited.insert(newNum);
      }
    }
  }

  return total;  
}



int main() {

  long long int LIMIT = pow(10, 9);

  auto start = chrono::high_resolution_clock::now();

  long long int answer = countHammingNumbers(100, LIMIT);
  auto end = chrono::high_resolution_clock::now();
  cout << "Answer: " << answer << endl;
  cout << "Time: " << chrono::duration_cast<chrono::milliseconds>(end - start).count() << " ms" << endl;
  return 0;
}

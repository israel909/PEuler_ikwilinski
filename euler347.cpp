#include <iostream>
#include <string>
#include <numeric>
#include <algorithm>
#include <vector>
#include <unordered_set>

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

// p must be less than q
long long int M(long long int p, long long int q, long long int N) {
  long long int currentNum = p * q;
  if (currentNum > N)
    return 0;
  if (currentNum == N)
    return N;
  int p_max = 1;
  long long int result = 0;
  for (; currentNum <= N;p_max++) {
    if (currentNum > N) {
      break;
    }
    else if (currentNum == N)
      return N;
    else if (currentNum > result)
      result = currentNum;
    currentNum *= p;
  }
  // We now have p_exp -> max
  long long int p_val = p;
  const long long int start_q_val = q * q;
  for (int p_exp = 1; p_exp < p_max; p_exp++) {
    currentNum = p_val;
    long long int q_val = start_q_val;
    for (; currentNum <= N;) {
      currentNum = p_val * q_val;
      if (currentNum == N)
        return N;
      else if (currentNum > result && currentNum < N)
        result = currentNum;
      q_val *= q;
    }
    p_val *= p;
  }
  return result;
}

long long int S(long long int N) {
  unordered_set<long long int> nums;
  vector<long long int> primes = genPrimes(N);
  cout << "Primes calculated successfully.\n";
  for (int p = 0; p < primes.size(); p++) {
    for (int q = p + 1; q < primes.size(); q++) {
      long long int value = M(primes[p], primes[q], N);
      if (!value)
        q = primes.size() + 1;
      else
        nums.insert(value);
    }
  }
  long long int answer = 0;
  for (unordered_set<long long int>::iterator itr = nums.begin(); itr != nums.end(); ++itr) {
    answer += (*itr);
  }
  return answer;
}

// 10000000
int main() {
  cout << "LIMIT: ";
  long long int N;
  cin >> N;
  long long int answer = S(N);
  cout << "ANSWER: " << answer << endl;
  return 0;
}

#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <numeric>
#include <limits>

using namespace std;

long findBestWithNum(int **data, int size, int row, int col) {
  long best = 0;
  long total = 0;
  int tau = 1;
  for (int r = row; r < size; r++) {
    for (int c = col; c < col + tau; c++) {
      total += data[r][c];
    }
    if (total < best)
      best = total;
    tau++;
  }
  return best;
}

long minSum(int **data, int size) {
  long best = 0;
  for (int r = 0; r < 50; r++) {
    for (int c = 0; c < r + 1;c++) {
      long candidate = findBestWithNum(data, size, r, c);
      if (candidate < best)
        best = candidate;
    }
    // cout << "Row " << r << " complete.\t" << "BEST: " << best << endl;
  }
  return best;
}


int main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("Usage: ./euler150 <input_filename>\n");
    exit(1);
  }
  string fileName = argv[1];
  ifstream input_file(fileName);
  int size;
  input_file >> size;
  cout << "Pyramid has " << size << " rows." << endl;
  int **pyramid = new int*[size];
  for (int r = 1; r < size + 1; r++)
    pyramid[r - 1] = new int[r];
  for (int r = 0; r < size; r++) {
    for (int c = 0; c < r + 1; c++) {
      input_file >> pyramid[r][c];
    }
  }
  input_file.close();
  cout << "Input file processed successfully." << endl;
  int answer = minSum(pyramid, size);
  cout << "ANSWER: " << answer << endl;
  for (int r = 0; r < size; r++)
    delete pyramid[r];
  delete [] pyramid;
  return 0;
}

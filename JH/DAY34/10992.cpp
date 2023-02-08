#include <iostream>
using namespace std;

int main() {
	int num;
	cin >> num;
	for (int i = 1; i <= num; i++) {
		if (i == num) {	for (int i = 1; i <= 2*num-1; i++) cout << "*"; }
		else {
			for (int j = num - i; j > 0; j--) { cout << " "; } 
			cout << "*";
			if (i != 1) {
				for (int j = 1; j <= (i - 1) * 2 - 1; j++) { cout << " "; }
				cout << "*";
			}
		}
		cout << endl;
	}
	return 0;
}
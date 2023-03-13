#include <iostream>
#include <string>

using namespace std;

int main() {
    string line;
    cin >> line;
    int floor = 0, basement = 0, i = 1;
    for (char ch : line) {
        if (ch == '(') {
            floor++;
    	} else {
            floor--;
	}
        if (basement == 0 && floor == -1) {
            basement = i;
        }
        i++;
    }
    cout << "Part One: " << floor << "\n";
    cout << "Part Two: " << basement << "\n";
    return 0;
}

#include <iostream>
#include <string>
#include <set>

using namespace std;

int main(){
	string str;
	set <string> my_set;
	while ( cin >> str ){
		if (str == "random_item_to_block"){
			continue;
		}
		my_set.insert(str);
	}
	set<string>::iterator it;
	cout << "[";
	for (it = my_set.begin() ; it != my_set.end() ; it ++ ){
		cout << "\"";
		cout << *it << "\", ";
	}
	cout << "]";
}
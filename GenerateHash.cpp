// GenerateHash.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "boost/regex.hpp"
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <boost/algorithm/string.hpp>
#include "unordered_map"
using namespace std;
using namespace boost;

int main()
{
	//match all email addresses.
	regex pattern("[_a-zA-Z\\d\\-\\./]+@[_a-zA-Z\\d\\-]+(\\.[_a-zA-Z\\d\\-]+)+");
	cout << pattern << endl;
	unordered_map<string, int> test;  //store one person owns how many eamils. 
	string buffer;
	ifstream rowfile ("mediumOutput.txt");
	ofstream outfile("FinalOutput.txt");
	if (! rowfile.is_open())
	{ cout << "Error opening file"; exit (1); }
	if (! outfile.is_open())
	{ cout << "Error opening file"; exit (1); }
	//output rows which start as From: or To:
	while (! rowfile.eof() ) {
		getline (rowfile,buffer);
		//string str_1 = "From:	Charlie Klein <cklein2@bellsouth.net>;Charlie Klein <cklein2@bellsouth.net>";
		boost::to_lower(buffer);
		//cout<<str_1<<endl;
		string::const_iterator start = buffer.begin();
		string::const_iterator end = buffer.end();

		smatch mat;
		while(regex_search(start, end, mat, pattern))
		{  
			string msg(mat[0].first, mat[0].second);
			unordered_map<string, int>::iterator it; 
			it = test.find(msg);  
			if(it==test.end())
				test.insert(pair<string, int>(msg, 1)); 
			else
				it->second +=1;
			//cout << msg << endl;

			start = mat[0].second;
		}  
	}	

	unordered_map<string, int>::iterator it;  
	/*
	for (it = test.begin(); it != test.end(); it++)  
	{  
		cout<<it->first<<"    "<<it->second<<endl;
	}
	*/  


	for (it = test.begin(); it != test.end(); it++)  
	{  if(it->second >=10)
		outfile<<left<<setw(40)<<it->first<<"	"<<it->second<<endl;
	}  

	rowfile.close();
	outfile.close();
	cout << "outFile generates success." << endl;

	/*
	string str_1 = "From:	Roy Callahan <call6603@bellsouth.net>";
	string str_2 = "Fom: Roy Callahan <call6603@bellsouth.net>";
	string str_3 = "From:Roy Callahan <call6603@bellsouth.net>";
	string str_4="To:	Bob Rose; cmorris@entercom.com; smith.rod.web@leg.state.fl.us; cretul.larry@myfloridahouse.com; fl_governor@myflorida.com; 'Senator Bob Graham'; senator@billnelson.senate.gov";
	vector<string> strings;
	strings.push_back(str_1); strings.push_back(str_2);
	strings.push_back(str_3);  strings.push_back(str_4); 


	for(int n = 0 ; n < 4 ; ++n)
	if(regex_match(strings[n], pattern))
	cout << strings[n] << " is matched" << endl;
	*/
	return 0;
}




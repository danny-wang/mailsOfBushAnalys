// splitFile.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "boost/regex.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <io.h>
#include <stdlib.h>
#include <sstream>
using namespace std;
using namespace boost;
int _tmain(int argc, _TCHAR* argv[])
{
	regex pattern1("^Subject:\\s+.+");
	regex pattern2("^From:\\s+.+");
	string rowFile="emails.txt";
	string buffer;
	ifstream rowfile(rowFile);
	if(!rowfile)
	{
		cerr<<"open file error"<<endl;
		exit(-1);
	}
	int i=1;
	while (! rowfile.eof() ) {
		getline (rowfile,buffer);
		
		if (regex_match(buffer, pattern1)){
		stringstream a;
		a<<"output\\"<<i<<".txt";
		string curr =a.str();
		cout<<curr<<endl;
		ofstream output(curr);
		output<<buffer<<endl;
		getline (rowfile,buffer);
		while(!regex_match(buffer, pattern2)){
			output<<buffer<<endl;
			getline (rowfile,buffer);
		}
		output.close();
		cout<<curr<<"file close"<<endl;
		i++;
		}
		else cout<<"do nothing"<<endl;
	}
	rowfile.close();
	return 0;
}


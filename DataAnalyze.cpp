// DataAnalyze.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "boost/regex.hpp"
#include <iostream>
#include <fstream>
#include <string>
#include <io.h>
#include <stdlib.h>
using namespace std;
using namespace boost;

regex pattern("^((From)|(To)):\\s+.+");
string buffer;
ofstream out;

void extractUsefulInfo(string in_name){

	ifstream rowfile(in_name);
	if(!rowfile)
	{
		cerr<<"open file error"<<endl;
		exit(-1);
	}
	while (! rowfile.eof() ) {
		getline (rowfile,buffer);
		if (regex_match(buffer, pattern))
		//cout << buffer << endl;
		out << buffer<<endl;
	}
	rowfile.close();

}


int main()
{	// "\w+\s*(\(\w+,\d+\)\s*)*"
	//regex pattern("\\w+\\s*(\\(\\w+,\\d+\\)\\s*)*");
	// ^From:\s+.+
	
    cout << pattern << endl;
	
	out.open("mediumOutput.txt",ios_base::app);
    if (! out.is_open())
		{ cout << "Error opening file"; exit (1); }
    
	struct _finddata_t fileinfo;
	string in_path;
	string in_name;
	cout<<"please input filefolder name: ";
	cin>>in_path;
	string curr = in_path+"\\*.txt";
	long handle;
	if((handle=_findfirst(curr.c_str(),&fileinfo))==-1L)
	{
		cout<<"没有找到匹配文件!"<<endl;
		return 0;
	}

	else
	{
		in_name = in_path + "\\" + fileinfo.name ;
		extractUsefulInfo(in_name);
		while(!(_findnext(handle,&fileinfo)))
		{
			in_name = in_path + "\\" +fileinfo.name;
			cout<<in_name<<endl;
			extractUsefulInfo(in_name);
		}
		_findclose(handle);
	}
    //ifstream rowfile ("2004b_July-Dec_GovernF-NRN.txt");
	
	out.close();
    cout << "Finish Generate Output File.!" << endl;
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



// tfidf.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

#include<map>
#include <set>
#include<string>
#include<iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
map<string,float> IDFTable;
struct Words{
    string wd;
    float freq;
    float weight;
};
bool cmp(Words &w1,Words&w2)
{
    return w1.weight>w2.weight;
}
map<string,int> WordTable;
vector<Words> WordList;
char Comment[]=",.!\"?;:()";
int totalText=0;
bool IsAllNumber(string cs)
{
    for (int i=0;i<cs.length();i++)
    {
        if(cs[i]<'0'||cs[i]>'9')
            return false;
    }
    return true;
}
bool Isblank(string cs)
{
    for (int i=0;i<cs.length();i++)
    {
        if(cs[i]!=' '&&cs[i]!='\t')
            return false;
    }
    return true;
}
string &ToLower(string &cs)
{
    for (int i=0;i<cs.length();i++)
    {
        if(cs[i]>='A'&&cs[i]<='Z')
            cs[i]+=('a'-'A');
    }
    return cs;
}
void readFile(string fname,set<string> &wds)
{
    ifstream fin(fname.c_str());
    string word;
    wds.clear();
    while (!fin.eof())
    {
        fin>>word;
        for (int i=0;Comment[i]!=0;i++)
        {
            int pos;
            while((pos=word.find(Comment[i]))!=-1)
            {
                word.replace(pos,1,"");
            }
        }
        //the world;
        if(!IsAllNumber(word)&&!Isblank(word))
        {
            wds.insert(ToLower(word));
        }
        /*totalwords++;
        */
    }
    fin.close();
}

void GenerateIDF()
{
    totalText=0;
    string files[5]={"p1.txt",
        "p2.txt",
        "p3.txt",
        "p4.txt",
        "p5.txt"
       };
    int x;
    set<string >wds;
    for (int i=0;i<5;i++)
    {
        readFile(files[i],wds);
        for (set<string>::iterator it=wds.begin();it!=wds.end();++it)
        {
            map<string,float>::iterator iter;
            string word=*it;
            if((iter=IDFTable.find(word))!=IDFTable.end())
            {
                iter->second+=1;
            }
            else
            {
                IDFTable[word]=1;
            }
        }
        totalText++;
		cout<<totalText<<endl;
    }
    //
    int cnt=0;
    for (map<string,float>::iterator iter=IDFTable.begin();iter!=IDFTable.end();++iter)
    {
        iter->second=log((float)totalText/(iter->second+1.0));
        /*cout<<iter->first<<' '<<iter->second<<endl;
        cnt++;
        if(cnt%100==0)
        {
            cin>>x;
        }*/
    }
}
int GenerateTF(){
    ifstream fin("Test.txt");
    string word;
    int textwords=0;
    while (!fin.eof())
    {
        fin>>word;
        for (int i=0;Comment[i]!=0;i++)
        {
            int pos;
            while((pos=word.find(Comment[i]))!=-1)
            {
                word.replace(pos,1,"");
            }
        }
        if(!IsAllNumber(word)&&!Isblank(word))
        {
            //wds.insert(ToLower(word));
            textwords++;
            ToLower(word);
            map<string,int>::iterator it;
            if((it=WordTable.find(word))!=WordTable.end())
            {
                it->second++;
            }
            else
            {
                WordTable[word]=1;
            }
 
        }
         
         
    }
    fin.close();
    //计算频率
    for (map<string,int>::iterator it=WordTable.begin();it!=WordTable.end();++it)
    {
        Words wd;
        wd.wd=it->first;
        wd.freq=(float)(it->second)/textwords;
        float idf=0;
        map<string,float>::iterator iter;
        if((iter=IDFTable.find(wd.wd))!=IDFTable.end())
        {
            idf=iter->second;
        }
        else
            idf=log((float)totalText);
        wd.weight=wd.freq*idf;
        WordList.push_back(wd);
    }
 
    return textwords;
}
void GenerateSort()
{
    sort(WordList.begin(),WordList.end(),cmp);
}
int main(){
    GenerateIDF();
	cout<<"asdfsadf"<<endl;
    int txtwd=GenerateTF();
	cout<<"asdfsadf"<<endl;
    GenerateSort();
	cout<<"asdfsadf"<<endl;
    int topnum=10;
    cout<<"Total Words: "<<txtwd<<" Top "<<topnum<<":\n";
    cout<<"Wrod\t\tWeight\n";
    for (int i=0;i<topnum;i++)
    {
        cout<<WordList[i].wd<<"\t\t"<<WordList[i].weight<<endl;
    }
}
#include <bits/stdc++.h>
#include<iostream>
#include<string>
#include<stdlib.h>
using namespace std;

 bool pallindrome_check(string w){

    std::string::iterator it; 
    std::string::reverse_iterator it1; 
  
    for (it=w.begin(),it1=w.rbegin(); it!=w.end(); it++,it1++) 
    if (*it != *it1){
        return false;
    }  
    return true;
  
}

bool pallindrome_checkAnswer(string b, string c){
    bool B = pallindrome_check(b);
    bool C = pallindrome_check(c);

    if (B && C){
        return true;
    }
    else{
        return false;
    }
 }


int main()
{
    
    string one,two,three;
    string input;
    int flag =1;
    cin>>input;
    
    int len = input.length();
    
    for(int i=0; i<len-2;i++){

        one = input.substr(0,i+1);
        if(pallindrome_check(one)){

        for(int j=0; j<len-i-2;j++){
            
            two= input.substr(i+1,j+1);
        
            three= input.substr(j+i+2, len-(j+i+2));
        

            if(pallindrome_checkAnswer(two,three) == true){
                 cout<<one<<"\n"<<two<<"\n"<<three;
                flag =0;
                exit(0);
            }
               
        }

            
        }
    }

    if (flag){
        cout<<"Impossible";
    }
}
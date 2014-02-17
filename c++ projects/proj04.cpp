/* 
 * File:   proj04.cpp
 * Author: James Mitchell
 *
 * Created on February 14, 2014, 2:21 PM
 */

#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cmath>
#include<cctype>
#include<typeinfo>

using std::cout; using std::cin; using std::endl;
using std::ifstream; using std::ofstream;
using std::istringstream; using std::ostringstream;
using std::string; using std::begin; using std::end;
using std::isalpha; using std::tolower;
using std::swap; using std::stol; using std::to_string;



/*
 * Given a start number, finish number and a limit
 * Find how many Lychrel, natural occuring palindrome numbers and regularly found palindrome numbers(using the algorithm within the given limit)
 */

long rev_num(long n){   //Reverses the order of the string, returns that reversed string as a number
    long temp = n;
    string temp_string=to_string(temp);
    string reverse_string = string(temp_string.rbegin(), temp_string.rend());
    long reverse_num = stol(reverse_string);
    return reverse_num;
}

bool is_palindrome(long n){
    long temp=n;
    long r;
    long sum=0;
    string perfect = to_string(n);
    if(equal(perfect.begin(), perfect.begin()+perfect.size()/2, perfect.rbegin())){
        return true;
    }
    else{
        return false;
    }
}

void order_parameters(long &first,long &second){    //function returns void, therefore need to pass arguments as reference
    if (second<first){
        swap(first,second);
    }
}

bool check_lychrel(long n, long limit){         //returns true if number of iterations exceeds the limit, false otherwise
    long sum=n;
    for(long count=0;count<limit;count++){      //can also be less than and equal to...
        if(is_palindrome(sum)==true){
            return false;       //Means it is a palindrome
        }
        long reverse_num=rev_num(sum);
        sum=sum+reverse_num;
    }
    return true;        //Means could not "convert to palindrome"
}

long check_range(long start, long end, long limit, long &natural_cnt, long &pal_cnt){
    long total_lychrel=0;
    order_parameters(start,end);
    for(long num=start; num<=end; num++){
        if(check_lychrel(num,limit)==true){
            cout<<"Found a lychrel number:"<<num<<endl;
            total_lychrel++;
        }
        else{
            pal_cnt++;
        }
        if(is_palindrome(num)==true){
            natural_cnt++;
        }
    }
    return total_lychrel;
}

int main() {
    long start_in;
    long finish_in;
    long limit_in=0;
    long total_lychrel=0;
    long natural_cnt=0;
    long pal_cnt=0;
    long temp_limit=0;
    
    while(true){
        
        cout << "Give me a start:  ";
        cin >> start_in;
        cout << "Give me a finish: ";
        cin >> finish_in;
        cout << "Give me a limit:  ";
        cin >> limit_in;

        if(start_in<1 || finish_in<1 || limit_in<1){     //Skips this iteration of the loop,and reprompts for other numbers
            cout<<"All inputs must be greater than or equal to 1, please try again!"<<endl;
            continue;
        }
        
        total_lychrel=check_range(start_in, finish_in, limit_in, natural_cnt, pal_cnt);
        cout<<"Summary for range "<<start_in<<", "<<finish_in<<" with limit:"<<limit_in<<endl;
        cout<<"Lychrel count:"<<total_lychrel<<", Natural count:"<<natural_cnt<<", Palindrome count:"<<pal_cnt-natural_cnt<<endl;
        break;
    }
    
    return 0;
}


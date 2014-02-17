/* 
 * File:   proj03.cpp
 * Author: James Mitchell
 *
 * Created on January 31, 2014, 3:41 PM
 */

#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>

// using declarations
using std::cin;
using std::cout;
using std::pow;
using std::endl;
using std::string;
using std::swap;


void order_parameters(double &first,double &second){    //function returns void, therefore need to pass arguments as reference
    if (second<first){
        swap(first,second);
    }
}

bool narc_num(double num,double power){
    int digits = num;
    double count = 0;
    double sum = 0;
    while(digits !=0){  //counting the number of digits in the number
        count++;
        digits/=10;
    }
    digits=num;
    while(digits!=0){
        sum += pow((digits%10), power);  //count==power
        digits/=10;
    }
    if(sum == num)
        return true;
    return false;
}

int check_range(double first,double last,double power){
    order_parameters(first,last);
    int total=0;
    for(int counter = first; counter < last; counter++){
        if(narc_num(counter,power)==true){
            cout << counter << " is a narcissistic number of order:" << power << endl;
            total++;
        }
    }
    return total;       //total number of N#'s found
}

/*
 * Program continuously looping user prompt, if the range and power given are greater than 0 the loop continues
 * The loop continuously checks the range for possible narcissistic numbers
 * Then prints the total #'s found with in the range given (in what ever order the user listed them)
 */
int main() {
    double first=1;		// User input numbers
    double last=1;	
    double user_pow=1;
    int total;
    
    while(first>0 && last>0 && user_pow>0){
        cout <<""<<endl;        //blank line
        cout << "Input of any value 0 or less stops the program"<<endl;
        cout << "give space separated start stop power:";
        cin >> first >> last >> user_pow;
        if(first>0 && last>0 && user_pow>0){
            total=check_range(first,last,user_pow);
            cout<<"Saw "<<total<<" order "<<user_pow<<" narc numbers in the range "<<first<<" to "<<last<<endl;
        }
    }  
    cout<<"thanks for playing"<<endl;   //Only runs when the loop ends (given proper input <0)
    
    return 0;
}



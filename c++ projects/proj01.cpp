/* 
 * File:   proj01.cpp
 * Author: James M.
 *
 * Created on January 19, 2014, 10:48 PM
 */

#include <iostream>
#include <string>

// using declarations
using std::cin;
using std::cout;
using std::endl;
using std::string;


/*
 * 
 */
int main() {
    double debt;
    int den;
    double pop;
    double miles;
    
    cout << "What is the national debt in dollars?: ";
    cin >> debt;
    cout << "Enter the denomination of the U.S currency bills you want to use: ";
    cin >> den;
    cout << "Enter the population of the U.S: ";
    cin >> pop;
    miles = ((debt/den)*(.0043))/63360;
    cout << "Miles high of indicated currency: " << miles << endl;
    cout << "Multiples of distance to the moon: " << 238857/miles << endl;
    int total=(debt/pop)+0.5;
    cout << "What each person owes: " << total;
    
    return 0;
}


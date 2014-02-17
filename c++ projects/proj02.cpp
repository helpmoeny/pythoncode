#include <iostream>
#include <math.h>
#include <string>

// using declarations
using std::cin;
using std::cout;
using std::endl;
using std::string;

/*
 * Program prompting for a number above 4 and event, then tells you what that numbers
 * prime components are and continuously re-prompts until told not to
 */
int main() {
	long prime1=1;
	long prime2=1;
	long is_prime1;
	long is_prime2;
	long user;		// User input number
        long i;
	long counter;


        while(user!=0){
                cout << "Give me an even number >= 4 or 0 to quit:";
                cin >> user;
                
                for (counter = 1; counter <= user; counter++) {
                    if(user<4 || user%2 != 0){
                        cout << "Number must be even and >= 4, try again!" << endl;
                        break;
                    }
                        prime1 = prime1 + 1;		

                        is_prime1 = true;					//checks to see if prime1 is a prime
                        for (i = 2; i <= sqrt((double)prime1); i++) {
                                if (prime1 % i == 0)
                                        is_prime1 = false;
                        }

                        if (is_prime1 == true) {                                // if prime1 is a prime then check to see if prime2 is a prime
                                prime2 = user - prime1;
                                is_prime2 = true;				
                                for (i = 2; i <= sqrt((double)prime2); i++) {
                                        if (prime2 % i == 0)
                                        is_prime2 = false;
                                }
                        }

                        if (is_prime1==true && is_prime2==true) {               // if prime1 and prime2 are both prime
                            if (prime1 + prime2 == user){			// and if prime1 + prime2 = the user, then print
                                if (prime2 >= 2) {
                                    cout << "The number:" << user << " is the sum of the primes:" << prime1 << ',' << prime2 << endl;
                                    break;
                                    }
                                }
                            }
                }
                prime1=1; //reset the prime numbers
                prime2=1;
            }
        cout<<"Thanks for playing"<<endl;
return 0;

}
//resources
#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <ctime>
#include <thread>
#include <chrono>
//#include <windows.h> doesn't work, as this codespace is not running on windows
#include <unistd.h>
//#include "ansi_escape_code.hpp"
using namespace std;
//using namespace ansi_escape_code;
//global variables
string redColor = "\033[0;31m";
string redBackground = "\033[41m";
string reset = "\033[0m";
string blueColor = "\u001B[34m";
string boldBlueColor = "\033[1;34m";
string boldRedColor = "\033[1;31m";
string redItalics = "\033[31;49;3m";
string greenColor = "\u001B[32m";
string greenBackground = "\u001B[42m";
string greenItalics = "\033[32;3m";
string yellowColor = "\u001B[33m";
string yellowBackground = "\u001B[43m";
string cyanColor = "\u001B[36m";
string boldCyanColor = "\033[36;49;1m";
string blueBackground = "\u001B[44m";
string blackColor = "\u001B[30m";
string brightYellowColor = "\033[0;93m";
string cyanBackground = "\033[46m";
string boldWhiteColor = "\033[1;37m";
string italics = "\033[3m";
string clear = "\033[H\033[2J";
//functions
void wait(int time) {
    usleep(time * 1000000);
}
/*void text(string text = "Hello World", int delay = 0.1, bool enterAfterDone = true) {
    for (char i: text) {
        cout << i << flush;
    }
}*/
int main() {
    cout << "testing\n";
    cout << "will it work?\n";
    wait(3);
    cout << "timer works";
    text("hope this works");
}
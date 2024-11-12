//resources
#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <ctime>
#include <thread>
#include <chrono>
#include <cstdlib>
//#include <windows.h> doesn't work, as this codespace is not running on windows
#include <unistd.h>
//#include "ansi_escape_code.hpp"
using namespace std;
//using namespace ansi_escape_code;
//global variables
bool game = true;
int roomNum = 0;
bool sideOpen = false;
const int menu = 0;
const int intro = 1;
const int room = 2;
const int computerOn = 3;
//terminal variables
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
typedef string::const_iterator iter;
//functions
/*void wait(int time) {
    this_thread::sleep_for(chrono::seconds(time));
}
void text(string text = "Hello World", int delay = 0.1, bool enterAfterDone = true) {

    iter begin = text.begin();
    iter end = text.end();
    for (iter it = begin; it != end; ++it) {
        cout.put(*it);
        this_thread::sleep_for(chrono::seconds(delay));
    }
}
*/
int main() {
    while (game == true) {
        //menu
        if (roomNum == menu) {
            string begin;
            cout << "░▒▓███████▓▒░░▒▓█▓▒░       ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓" << "▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░ \n" << "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░" << "▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ \n" << "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░" << "▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ \n" << "░▒▓███████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░" << "▒▓█▓▒░░▒▓██████▓▒░  \n" << "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░" << "▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ \n" << "░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░" << "▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ \n" << "░▒▓███████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░ ░▒▓████" << "██▓▒░░▒▓█▓▒░░▒▓█▓▒░ \n";
            cout << "Begin? [Y/N]\n";
            cin >> begin;
            if (begin == "y" || begin == "y") {
                cout << "Let's begin.\n";
                usleep(2*1000000);
                cout << clear;
                roomNum = 1;
            }
            else if (begin == "n" || begin == "N") {
                cout << "Not like you had a choice anyway.";
                this_thread::sleep_for(chrono::seconds(3));
            }
        }
        else if (roomNum == intro) {
            cout << greenItalics << "Wake up. Get on your feet.";
            this_thread::sleep_for(chrono::seconds(3));
            cout << clear;
            cout << "You need to wake up.";
            this_thread::sleep_for(chrono::seconds(3));
            cout << clear << reset << italics << "You pick yourself up off the floor.";
            this_thread::sleep_for(chrono::seconds(3));
            cout << clear << "You can't remember who you are, where you came from, or how you got here. You don't even remember your own name.";
            this_thread::sleep_for(chrono::seconds(5));
            cout << clear << "You find yourself in a square room with no windows, no doors, and no furniture. The floors are covered in a black carpet.";
            this_thread::sleep_for(chrono::seconds(6));
            cout << clear << "That is, except for a desk bolted to one of the walls and a singular ventilation shaft.";
            this_thread::sleep_for(chrono::seconds(5));
            cout << clear << "There is a lamp on the desk (thank god, you wouldn't be able to see otherwise) and an old-looking CRT monitor.";
            this_thread::sleep_for(chrono::seconds(5));
            cout << clear << "The case of the monitor is white, along with the keyboard. No mouse though. Strange.";
            this_thread::sleep_for(chrono::seconds(6));
            cout << clear << "Then, you hear a disembodied voice.";
            this_thread::sleep_for(chrono::seconds(4));
            cout << clear << "It says:\n\"Welcome, welcome! Welcome to our facilities! This is where you will be spending the next " << boldRedColor << "[FLOAT OVERFLOW]" << reset << " days! The only thing we ask of you is that you test the terminal installed on the computer on the desk. We" << italics << " would " << reset << "have used a more modern monitor, but some budget cuts happened. Y'know how it is. Anywho, good luck! Enjoy your stay!";
            this_thread::sleep_for(chrono::seconds(10));
            cout << clear << "...what..?";
        }
    }
}
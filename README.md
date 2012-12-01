
Robot-Bomb-Defuser-Game
=======================

A game written in python language using the curses library.


Description of the Game
=======================

The game is played in a square grid called the field. A robot moves in the field and cannot go outside the field.

The field has a bomb which you have to defuse. In order to defuse a bomb, the robot must have 6 defuse codes. Each of these codes contains vital information on how to defuse the bomb.

The field has exactly 6 diffuse codes located at random positions. The user should move the robot around in order to collect these codes. When a robot approaches a diffuse code, it collects the code automatically.

When a robot approaches a bomb, the following things may happen

--->if the robot has exactly 6 defuse codes, the bomb is defused. The user gets 6 points for this.
--->if the robot has less than 6 defuse codes, the bomb explodes and the game ends.

The game consists of 4 levels. With each level the difficulty level increases.Once the bomb is successfully defused in all the levels, the game ends and you win the trophy.


Dependencies 
============

Requires Python2.7 (http://www.python.org/)


How to use
==========

After downloading the source file, type in the terminal:

  > python robot.py
Hacker-Academy-Competition-Final-Maze-Problem
=============================================

Solution to a maze problem given as the final problem on a Hacker Academy competition.

###About Hacker Academy
[Hacker Academy](hackeracademy.org) is a group based in Toronto which conducts programming competitions and
hackathons. The academy has previously gotten sponsorship of tech organizations like NewEgg and Microsoft.

###The Programming Competition
The competition held back in November of 2012, comprised of 3 problems (problem 0,1 & 2). Hackers were given
3 hours to complete these 3 problems. The faster you happened to complete them the more points you would get. Each
problem has a small input sample to test on, and a large input one which was the dataset on which you would have
to provide the solution (within 300 seconds). The first
two problems were trivial, however the thid one was one of those typical maze problems you'd find in popular programming
competitions every now and then.

###The Ubiquitous Maze Problem
The third and final problem dealt with a maze problem. A screenshot of the problem is present in the
repo, named [maze_problem.png](maze_problem.png). However in a nutshell; we were given a maze like the following:

    ___________
    |_    |  _|
    |  _| |_  |
    |   |___  |
    | |_  |  _|
    |_|___|___|
  

Starting from the top left spot in the maze, a path had to be found to the bottom right. The path had to created
using directions North (N), East (E), South (S), West (W). For example the above maze problem has the solution:

    1E 1E 1S 1S 1E 1E 1S 1W 1S 1E
  
If there existed no possible route then the correct solution would be -1.  
Given the small size of the above maze the solution could easily be hard coded, even within the 300 second limit, however
the above maze was simply given as an example to demonstrate the problem. The large inputs looked like this:

    _____________________________________________________________________________________________________________________________________________
    |   |_____  |  _    | |   |_   _  | |  ___   _|  _    |_    | |  _   ___|  ___    |_   _  |   |_____   _  |  _   _  |_    |  ___   _|  ___  |
    | |___  |  _| | | |_  | | |  _| | | | |   |_____| | |_____| |_____| |  _______| |_  | | | | |_________|  _|_|  _| |  ___| |_____|   | |_  | |
    |   |_  |_______| |___| |___| |  _|  ___|_______  | |    _|_  |   |  _|  _  |   |_____| | | |  _____  |_____  |_____|   |_____  |_| | |   | |
    |_|_  |_  |    ___|  ___|  ___|_  |_|   |   | |  _| |_|  _  | | | |  _| |  _| |_|   |  ___|  _|_    |___  |___|  _____|_  |_  |_  |  _| | | |
    |  ___|_____|_|   | |  ___|   |  _|  _|___| | |_  |_  |_  | | | | |_|  _|_  | |  _| | |  _| |   | |___  |_  |  _|  ___|  _|   |  _|_____|_| |
    | |   |   |  ___|___|  _____| |_  |_  |   | |  ___| |_  |_|_____|_____|  _| |  _|  _| | |  _| | |_  |  _  |___|___  |  _|  _|_| |  _  |  _  |
    | | |___| | |  _  |_________|   |_  | | |_| |_  |    _| |  _  |  _  | |  ___|_  | | | |  _|  _| | | | |_  |_    |   | |  ___  |___| |___|  _|
    |  _|   | |___|___|  ___  |  _| | |___|_  | | |___| |  _|_  |___| | | |_  |_____| | | |_  | | | | | |_  |_____| | | | |_|  ___  |  _______  |
    |_|  _| |  ___  |  _|_  |___|  _|_   _  | | |_  |  _|_____________| |   | |  _____|  _| |___| | | | | |_____  |___| |_  | |_____| |  ___  | |
    |  _| | | |   |___|    _  | | |  ___|___  |_  |_____  |  ___________|_| | |   |   | |  _  |  ___|_________|  _|   |_|   |_________| |   | |_|
    | | |  _| | |_______| |  _| | |___   _  |___|_  | |  _| |  _______    | | |_| | | | |_  | |_  |_   _______  |  _|  ___|_|  ___    | | |_|_  |
    | | |_____|___|  _____|_  | | |   |  _| |  _  | |___|  _|_  |  _____| | |_____| | |_  | |_  |_  | |_________| |  _|   |  _|   | |_____|  _  |
    | |___     _____|   |  _|_  |___| | |   | | |___|  ___|  ___|_____  |___  |   | |  _| | |  ___| |  ___  |  ___|_  | | | |  _| |_  | |  _|___|
    | |   |_|   |  ___| |  ___  |  ___|_| |_|_________|  ___|___    | |_  |_  |_|___| |  _| |_|  ___|_____| | |   |  _| |___|_  | |_____|___    |
    | | |_  |_| |  ___| | |   |_|_____  | |  ___  |   | |    _____| |  _|_  |_______  | |   |  _|  _  |  ___| |_|___  |_  |  ___| |  _  |   |_| |
    | | |  _|  _| |  ___| | |_  |   |  _| | | |   | |___|_| |  _  | | |  ___|  _  |  _| | |_| |   |_____|  ___|  _  |_|  _|_  | | |_  |___| |   |
    | | |_  |   | | |_____| | | | | | |   |_  | |_|_________| | | | | |_  | |_  |___| | |_  |  _|_|  _  |___  |_  |_____|   | |  _|  _|_______| |
    |  _| | |_|  _|___  |  _| |___|___| |  _| |___________  |_  |_______| |_________  |_  |_  |   | | | |  ___|  _____  | |_| | |___   _____  |_|
    | |_  |_  |___   _| | |   |  ___|  _| |  _|_   ___    |_____|  _____  |  _  |  ___| |_  |_| |___|  _|_______|  _  | |_  | | |   |_|  _  |_  |
    |___   _|_  |___|   |___| | |  ___  | | |   |_____| |_____  | |  _  | |_  | |___  |   | |  _|_  |___  |  _  | | | |___  | |___|_  |_  |___  |
    |   | |  ___|   | | |  _| |  _|   |_| |___|_____  | |_  |  _|___| | |___| | |_   _| | | | |  _  |  _|___| | | |_  |_____| |_    | |  _|_____|
    | |___|_  |  _|___|_  |  _|_|  _| |  _____  |_  |___|   |_  |  _  |_______|_  |_____|_| | |   |___|  _  |  _|_  |_____  |_  | |___|  _____  |
    | |   |  _| |  ___  | |___   _|_____|_   _|_______  | | | | |___|  _  |___  |___________| | | |   | |  _|_______|    _|_____|_  | | |  _  | |
    | | |___|  ___|   | |_|   | |  _____  |  _   _____|___|_  | |   |_  |___  |_   ___  |_   _| |___|___| |  _________| |  _  |   | |  _|_  |_| |
    | | |   | |___  | |_  | |___|_  |_  | |_  | |  _______  | |___|_____|  _|_  |_  | | |  _| | |   | |  _| |_     ___|___| |___|___|___  |_  | |
    | | | | |_  |  _|_  |___|_  |  _|   | |  _|___  |  _  | | |  ___    |    _|_____| |___| |  _| |_  | |  _|  _|_|   |    _____  |    _|_  | | |
    |_| | |_  |___|  _|___  |  _| |_  | | | |   | | |_  | | | |_  | | |_| |_    | |  _____  |_  | |___| | |  _______|___| | |  ___|_|___   ___| |
    |  _| |  _|  ___  |  ___| |  _|  _|_| | | | |  _| | |___| | |_  |_____|  _| |___|  _  |  _| |  _  | | |___  | |  _____| |_  |    _  | |   | |
    |  ___| |_   ___| | |  ___|_   _|  ___|_| | |___  |___  | |   |_____  | |_________|  _|_  | | | | |___|  _____|   |_    |  _|_|_  | | | |_  |
    |  ___|   | |  ___|_  |   |  _|  _|  _  | | |_________|_  | |_  |  ___|___  | |   | |     | |_  |_  |  _|  _  |_|_  | |_|_________| |_|_  | |
    | |   |_| | |_  |  ___| | | | |_____| |___|_  |  _____  |___| | |_  |  _____|  _|_  |_| |_| |_   _|_____| |_  |  ___| |  _   ___  |_  |  _| |
    | | |_   _|___|_____|  _|___|  _   _________| | |     | |   | | |  _|_  |_____|   |_  |_  |_  |_|  ___  |   |___|_______|  _| |  ___| |_  | |
    | |_  | |  ___  |  ___|   |_____| |  _____  | | |_| | |___| |___| |   |_____  | | | |___  | |_____|  _| |_|___  |  _  |  _|  _|  _|  _|  _|_|
    | |  _| | |    _| |  ___|_______  |___  | | | |___  |_|  ___|  ___| | |  _|   | | |___  | |  ___  |   |_________|   |___| |  ___|  _|  ___  |
    | | |___| | |_|  _| |_     _|   | |_  | |_   ___|  _|  _|  _________|___|  _| | |___  | |___|   | | |  ___  |  _| |_  |   |___  | |  _____| |
    | |_  |  _| |  _|___  | |_____| |___  |_  |_|   | |  _|  _|  ___  |  _  |_  | | | |  _|    ___|_| |_| | |  ___|  _|  _| |_______| | |  ___  |
    | | | |_  |___|  _  | |_  |  _|_   _|_  |_____| | | |  _| |___  |___|_______| | | |_  |_|_   _________| | |  ___|  _|  _|  ___  | |_|_  |  _|
    | | |_  |_  |  _| | | | | |___  |___  | |_    | | |___|   |_  |___  |   |  _| |___  |___  |_|   |_____   _|___  | |_   _|_  | | | |  ___| | |
    |_  | |_____| |   | | | |_________  | |_  |_| | | |  ___|_  |___  | | | |_____|   |_  |  _|  _|_____  |_|   |  _|_  |_|   | | |___| | |  _| |
    |_____________|_|_____|_____________|_________|_____|_____________|___|_________|_____|_____________|_____|_______|_____|___________|_______|
  

###The solution
It took me close to an hour and a half to figure out the solution, which I implemented using Python. The code can
be broadly viewed as performing 2 tasks:
- **Codifying**: The input of the maze layout given as a txt file containing utf characters needed some
sort of abstraction into a dataset which a program could understand. `codify_maze(maze)` did this job.
- **Navigating**: With a data structure containing the maze now only the job of finding a path was remaining. Recursively
navigation the maze using a global data structure to hold the navigated of directions from the different spots of the maze
was left to `solve(maze,cur_row,cur_lev,collected)`





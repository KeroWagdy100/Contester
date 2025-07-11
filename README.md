# The cf Command

> C:\ProblemSolving\Contests> `cf new [.] [-m "ContestName"] [-t] --to f `

OR

> C:\ProblemSolving\Contests> `cf new [.] [-m "ContestName"] [-t] -n 6 `

OR

> C:\ProblemSolving\Contests> `cf new [.] [-m "ContestName"] [-t] -i 2119 `

* where **2119** is the contestId (last number (typically 4 digits) in the contest dashboard link)
* when `-m` is omitted and the contest id is not provided, the command asks you to name the contest
* if the `.` is omitted, the contest is created in the defaultContestPath (change it in Contester.config)
* `-t` is responsible for creating the files with a code snippet template (change it in Contester.config)

Let "ContestName" be "Div2"


This creates a new directory in the current directory
> C:\ProblemSolving\Contests\Div2\

This diretory has directories from A to F (Problems)
> C:\ProblemSolving\Contests\Div2\A  

> C:\ProblemSolving\Contests\Div2\B  

> ..   

> C:\ProblemSolving\Contests\Div2\F 

Each problem directory has a [problemLetter].[langExtension]
> C:\ProblemSolving\Contests\Div2\A\A.cpp  

> C:\ProblemSolving\Contests\Div2\B\B.cpp 


Now all problem files are ready for you to write into
Let's navigate through them easily!

`cf goto d`

This opens problem **D** on your favourite IDE (vscode by default, change ide in config section)

`cf goto --next` OR `cf goto `  
Opens next problem file  

`cf goto --prev`  
Opens previous problem file  


## Solve a Quickie
What if you wanna solve a quick problem? Easy, let's see how

> C:\ProblemSolving\Quick> `cf quick . [-m "problemName"]`  

if the `.` is omitted, the problem is created in the defaultProblemPath (change it in cf.config)

This creates a problem folder and a file **main.cpp**


---
You have another solution for the same problem? No problem!

` cf another [problemLetter] `  

if `problemLetter` omitted, another solution folder created in the current problem

# doif
need to automate doing something if something else?

* This is a snippet mainly playing the part in the scaffolding of a target based system, like say,  ... make .... that has `remedial actions` that need applying.
* the tool is python, and seems pretty cross platform, to my level of caring
* there is a test runner ./test.sh | test.bat and a test Makefile that has target dependencies and the actual "work done" driven by the variable `action`
* The end game is to do something like
    python doif.py "action=test make" "action=fix make" pass1 pass2 fixable1 fixable2 broken1 broken2
* the output will show of the list of targets, how many were tested, how many fixed, and how many failed to fix
* the return code will be zero if none of the targets failed to fix or pass the test

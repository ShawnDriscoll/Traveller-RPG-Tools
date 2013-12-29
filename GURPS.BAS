DIM dr(18)
RANDOMIZE
CLS

50 FOR i = 3 TO 18
    dr(i) = 0
NEXT i
PRINT
PRINT
100 INPUT "How many GURPS die rolls (0 to quit)? ", n
IF n < 0 THEN 100
PRINT
IF n = 0 THEN 500
FOR i = 1 TO n
    die1 = INT(RND * 6 + 1)
    die2 = INT(RND * 6 + 1)
    die3 = INT(RND * 6 + 1)
    PRINT die1; die2; die3
    roll = die1 + die2 + die3
    dr(roll) = dr(roll) + 1
NEXT i
PRINT
p = 0
FOR i = 3 TO 18
    PRINT i; dr(i);
    p = p + dr(i) * 100 / n
    PRINT dr(i) * 100 / n; "%"
NEXT i
PRINT "     "; p; "%"
GOTO 50
           
500 END


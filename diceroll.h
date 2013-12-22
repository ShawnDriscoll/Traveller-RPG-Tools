//	diceroll.h -- Called by solomani.c
//
//	Compile with TI-GCC for execution on a TI-89
//
//	Written by Shawn Driscoll
//	shawndriscoll@hotmail.com
//

int die_roll(int die)
{
	return random(die) + 1;
}

int roll(char dice[10])
{
	int value;
	int i;		
		
    if (dice[0] == 68)   // "D" is at beginning of roll string?
	{
		printf("D00 and D10 code goes here!\n");
		return 0;
	}
    else
	{
		if (dice[1] == 68)  // "D" is in middle of roll string?
		{
			if (dice[0] >= 48 && dice[0] <= 57)
			{
				value = 0;
				for (i = 1; i < dice[0] - 47; i++)  // Roll the number of dice
					value += die_roll(dice[2] - 48);  // Add this die roll type to the total
				return value;
			}
		}
	}
	printf("DICE ERROR!\n");
	printf("%s unknown\n", dice);
	return 0;
}
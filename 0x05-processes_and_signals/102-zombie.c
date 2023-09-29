#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - looping zombie
 * Return: 0 on success
 **/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main -entry pont for zombie program
 * Return: 0 on success
 **/
int main(void)
{
	pid_t child_pid;
	unsigned int zombie_counter;

	for (zombie_counter = 0; zombie_counter < 5; ++zombie_counter)
	{
		child_pid = fork();
		if (child_pid == -1)
		{
			fprintf(stderr, "Exiting...\n");
			return (1);
		}
		else if (child_pid == 0)
		{
			printf("Exiting Child ID process to create zombie...\n");
			exit(0);
		}
		else
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
	}

	infinite_while();

	return (0);
}

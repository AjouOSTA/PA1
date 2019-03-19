#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <sys/types.h>
#include <sys/wait.h>

#include <unistd.h>

int main()
{
	char buf[4096];

	while (fgets(buf, 4096, stdin)) {
		if (strncmp(buf, "pwd", 3) == 0) {
			pid_t pid = fork();
			int status;

			if (pid == -1) {
				fprintf(stderr, "Error occured during process creation\n");
				exit(EXIT_FAILURE);
			} else if (pid == 0) {
				char working_directory_name[4096];
				getcwd(working_directory_name, 4096);

				printf("%s\n", working_directory_name);

				exit(EXIT_SUCCESS);
			} else {
				waitpid(pid, &status, WNOHANG);
			}
		} else {
			printf("I don't know what you said: %s", buf);
		}
	}

	return 0;
}

#include <stdio.h>
#include <string.h>

#include "getopt.h"

int
main(int argc, char *argv[])
{
    int c;
    int fflag, bflag;

    fflag = bflag = 0;
    opterr = 0;

    while((c = getopt(argc, argv, "fb:")) != -1) {
        switch (c) {
            case 'f':
                printf("-f flag found\n");
                fflag = 1;
                break;
            case 'b':
                if (strcmp(optarg, "bar") == 0) {
                    printf("-b flag found, value: %s\n", optarg);
                    bflag = 1;
                }
                break;
            default:
                break;
        }
    }

    return (fflag == 1 && bflag == 1) ? 0 : 1;
}


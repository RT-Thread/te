#include <rtthread.h>
#include <finsh.h>

int ex1(int argc, char** argv)
{
    printf("testsuite example\n");
    return 0;
}
MSH_CMD_EXPORT(ex1, testcase example1);

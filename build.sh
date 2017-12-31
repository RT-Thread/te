./prepare.sh

# link testcase
if [ ! -d "rt-thread/bsp/qemu-vexpress-a9/testcase" ]; then
ln -s `pwd`/testcase rt-thread/bsp/qemu-vexpress-a9/testcase
fi

PWD=`pwd`
cwd=$PWD

cd rt-thread/bsp/qemu-vexpress-a9
scons --useconfig=$cwd/config/base_config
scons
cd $cwd

if [ ! -f "rt-thread/bsp/qemu-vexpress-a9/rtthread.elf" ]; then
echo "BUILD RT-Thread FAILED"
echo "BUILD           FAILED"
echo "BUILD           FAILED"
fi

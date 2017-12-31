if [ ! -f "sd.bin" ]; then
dd if=/dev/zero of=sd.bin bs=64M count=1
fi

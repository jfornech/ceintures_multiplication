cython3 ceinture4.py -o ceinture.c --embed
gcc -Os -I /usr/include/python3.5m  ceinture.c -o ceinture -lpython3.5m -lpthread -lm -lutil -ldl

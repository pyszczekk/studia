CC=g++

a.out: test.o
	$(CC) test.o

test.o: test.cpp bmp.h vec.h light.h ray.h obj.h sphere.h triangle.h objreader.h trace.h render.h readFile.h
	$(CC) -c test.cpp
clean:
	rm test.o
#stworzyc pliki z funkcjami i wywolac je w jednym mainie; 


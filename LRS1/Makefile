#LaSDAI

biblioteca = 32bits
dir = lasdai-ula/biblioteca/$(biblioteca)/pr1-ula.o lasdai-ula/ejemplos/
dir2 = lasdai-ula/biblioteca/$(biblioteca)/

ejecutables = ejemplo1 ejemplo2 ejemplo3 ejemplo4 ejemplo5 ejemplo6

all: ejemplos

ejemplos: $(ejecutables)

ejemplo1: 
	gcc $(dir)ejemplo1.c -o ejemplo1 -lpthread

ejemplo2: 
	gcc $(dir)ejemplo2.c -o ejemplo2 -lpthread

ejemplo3: 
	gcc $(dir)ejemplo3.c -o ejemplo3 -lpthread

ejemplo4: 
	gcc $(dir)ejemplo4.c -o ejemplo4 -lpthread

ejemplo5: 
	gcc $(dir)ejemplo5.c -o ejemplo5 -lpthread

ejemplo6: 
	gcc $(dir)ejemplo6.c -o ejemplo6 -lpthread

clean:
	rm -f $(ejecutables)

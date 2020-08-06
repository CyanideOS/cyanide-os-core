compiler = cl
compilerArgs = /std:c++latest /O1 /Ot

all: start build move clean

start:
	clear

build: utilities.dir

move:
	mkdir bin -p
	mv *.exe bin/

utilities.dir:
	$(compiler) utilities/mkdir.cpp $(compilerArgs) -o mkdir.exe

clean:
	rm -rf /f *.obj
	rm -rf /f *.pdb
	rm -rf /f *.ilk

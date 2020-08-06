compiler = cl
compilerArgs = /std:c++latest

all: start build move clean
	$(compiler) utilities/utilities.cpp $(compilerArgs) -o utilities.exe

start:
	clear

build: utilities

move:
	mv *.exe ./bin

utilities:
	$(compiler) utilities/utilities.cpp $(compilerArgs) -o utilities.exe

clean:
	rm -rf /f *.obj
	rm -rf /f *.pdb
	rm -rf /f *.ilk

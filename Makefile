# Before run this make, please define the environment variable ${PREFIX}
all: test
	echo "This is a Makefile wrapper, provide an install target to move everything under gufiwrappers to the ${PREFIX} path."

test:
	echo "This is a placeholder, nothing happens after make the target test."

#setenv PREFIX /path/to/gufiwrappers
install: 
	echo "PREFIX is: "${PREFIX}
	install -d ${PREFIX}/
	cp -r * ${PREFIX}/

# Makefile for Java Composition Example

# Variables
JAVAC = javac
JAVA = java
SRC = book.java library.java main.java
CLS = book.class library.class main.class

# Targets
all: compile

compile:
	$(JAVAC) $(SRC)

run: compile
	$(JAVA) main

clean:
	rm -f $(CLS)

.PHONY: all compile run clean

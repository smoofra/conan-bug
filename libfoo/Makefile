
RANLIB ?= ranlib

all: libfoo.a

libfoo.a: foo.o
	$(AR) ru $@ $<
	$(RANLIB) $@

foo.o: foo.c
	$(CC) -c foo.c -o foo.o

install: libfoo.a
	mkdir -p $(DESTDIR)/lib
	mkdir -p $(DESTDIR)/include
	cp foo.h $(DESTDIR)/include/foo.h
	cp libfoo.a $(DESTDIR)/lib/libfoo.a


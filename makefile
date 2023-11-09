NAME = dtep
PREFIX = /usr/local

default:
	@echo "run 'make install' to install $(NAME)"
install:
	cp ./$(NAME) $(PREFIX)/bin/$(NAME)
	chmod 755 $(PREFIX)/bin/$(NAME)
uninstall:
	rm $(PREFIX)/bin/$(NAME)

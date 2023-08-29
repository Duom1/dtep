NAME = dtep

default:
	@echo "run 'make install' to install applications"
install:
	cp ./$(NAME) /usr/local/bin/$(NAME)
	chmod 755 /usr/local/bin/$(NAME)

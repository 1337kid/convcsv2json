PROGRAM_NAME=csv2json
VERSION=1.1

PROGRAM_DIR=/usr/bin

install:
	install -Dm755 csv2json.py $(PROGRAM_DIR)/$(PROGRAM_NAME)
uninstall:
	rm -Rf $(PROGRAM_DIR)/$(PROGRAM_NAME)
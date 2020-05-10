all: tag

tag:
	ctags -R -f ./.git/tags .


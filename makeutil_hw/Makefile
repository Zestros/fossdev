.DEFAULT_GOAL := help

create-homework:
ifndef HOMEWORK
	$(error must pass val via HOMEWORK)
endif
	mkdir -p $(HOMEWORK)
	cp HOMEWORKMakefile $(HOMEWORK)/Makefile

remove-homework:
ifndef HOMEWORK
	$(error must pass val via HOMEWORK)
endif
	rm -rf $(HOMEWORK)
	

help:
	@echo "This makefile for repo-level activity"
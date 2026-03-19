.DEFAULT_GOAL := help


create-practice:
ifdef PRACTICE
	$(error must pass val via PRACTICE)
endif
	mkdir -p $(PRACTICE)
	#mkdir demo-practice/scr
	#mkdir demo-practice/tests
	#mkdir demo-practice/docx
	#touch demo-practice/README.md

remove-practice:
	rm -rf $(PRACTICE)

help:
	@echo "This makefile for repo-level activity"


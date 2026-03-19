help:
	@echo "This makefile for repo-level activity"

create-practice:
	mkdir demo-practice
	mkdir demo-practice/scr
	mkdir demo-practice/tests
	mkdir demo-practice/docx
	touch demo-practice/README.md

remote-practice:
	rm -rf demo-practice


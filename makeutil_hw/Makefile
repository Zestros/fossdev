.DEFAULT_GOAL := help


create-workspace:
ifndef PROJECT
	$(error must pass val via PROJECT)
endif
	mkdir -p $(PROJECT)
	mkdir -p $(PROJECT)/src $(PROJECT)/tests $(PROJECT)/docs
	@touch README.md setup.py requirements.txt $(PROJECT)/docs/DOMAIN.md
	@touch $(PROJECT)/src/.gitkeep $(PROJECT)/tests/.gitkeep
	@echo "Created"

remove-workspace:
ifndef PROJECT
	$(error must pass val via PROJECT)
endif
	rm -rf $(PROJECT)
	

help:
	@echo "This makefile for repo-level activity"
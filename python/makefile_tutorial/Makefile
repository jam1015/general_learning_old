VENV = venv 
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
# can replace variables by going make VENV=my_venv run
.phony run clean

run:
	python app.py

setup: requirements.txt
	pip instal -r requiremets.txt #can change the requirements in the textfile

clean:
	rm -rf __pycache__

$(VENV)/bin/activate: requirements.txt
	python3 -m $(VENV) $(VENV)
	./$(PIP) install -r requirements.txt

run: $(VENV)/bin/activate
	./$(PYTHON) app.py


clean:
	rm -rf __pychache__
	rm -rf $(VENV)

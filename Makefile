install:
	pip install -r requirements.txt

run:
	python3 main.py

test:
	python3 -m unittest discover tests -v

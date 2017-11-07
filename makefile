test:
	cd ./botQueToca/ && pytest
	cd ./botQueToca/ && nosetests
	hug -f hugweb_test.py

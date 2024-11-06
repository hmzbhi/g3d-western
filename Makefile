run:
	# Droits d'exécution
	chmod +x ./src/viewer.py

	# Exécution du programme
	./src/viewer.py

clean:
	rm -rf ./src/__pycache__/
	rm -rf ./src/pyobj/__pycache__/
	rm -rf ./src/tools/__pycache__/
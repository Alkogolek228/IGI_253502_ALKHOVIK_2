DJANGO := python3 manage.py 
run:
	$(DJANGO) runserver --insecure
migrate:
	$(DJANGO) makemigrations && migrate
stat:
	$(DJANGO) collectstatic
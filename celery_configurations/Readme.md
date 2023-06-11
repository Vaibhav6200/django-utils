*** Run these 3 commands in seperate terminals ***
python .\manage.py runserver
celery -A celery_configurations.celery worker --pool=solo -l info
celery -A celery_configurations beat -l info
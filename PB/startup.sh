source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations accounts
python3 manage.py makemigrations studios
python3 manage.py makemigrations
python3 manage.py migrate

echo "========> Applying migrations <========"
python manage.py migrate

echo "========> Creating superuser <========"
python manage.py createsuperuser --no-input \
        --username $DJANGO_SUPERUSER_USERNAME \
        --email $DJANGO_SUPERUSER_EMAIL

echo "========> Superuser created <========"
echo "Email: $DJANGO_SUPERUSER_EMAIL"
echo "Username: $DJANGO_SUPERUSER_USERNAME"
echo "Password: $DJANGO_SUPERUSER_PASSWORD"

echo "========> Starting server <========"
python manage.py runserver 0.0.0.0:8000
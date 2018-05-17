sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
gunicorn -c /home/box/web/etc/django.py wsgi
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
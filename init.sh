sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
sudo gunicorn -b 0.0.0.0:8080 hello:application
sudo gunicorn -b 0.0.0.0:8000 ask/ask/wsgi:application 

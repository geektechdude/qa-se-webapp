In a live or production environment the default FLASK server should not be used.

Gunicorn is a good alternative and can be installed in the Python Virtual Environment via:

pip install gunicorn==20.1.0

Gunicorn can then be set to run as a service by copying the assets.service file (modify the directory paths insde the file) to:

/etc/systemd/system

and then running the commands:

systemctl daemon-reload
systemctl start assets.service

This will then serve the FLASK application locally over port 8000. 

Nginx (or similar) can then be used to forward web traffic (80, 443) to this port.
An example Nginx config file is available as nginx_assets_example.

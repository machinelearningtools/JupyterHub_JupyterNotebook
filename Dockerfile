





FROM jupyterhub/jupyterhub:0.9.4
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m pip install --no-cache -r /tmp/requirements.txt
Run python3 -m pip install dockerspawner
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
EXPOSE 8000











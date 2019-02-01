# dummy for testing. Don't use this in production!
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

# Configuration file for jupyterhub.
import os
import socket
import kubespawner
# configuration for Auth0 authentication

c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'

c.JupyterHub.spawner_class = 'kubespawner.KubeSpawner'
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.cleanup_servers = False
c.KubeSpawner.start_timeout = 60 * 50
c.KubeSpawner.image = 'jupyter/all-spark-notebook:87210526f381'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host_ip = s.getsockname()[0]
s.close()
c.KubeSpawner.hub_connect_ip = host_ip
c.JupyterHub.hub_connect_ip = c.KubeSpawner.hub_connect_ip
c.KubeSpawner.service_account = 'default'
#c.KubeSpawner.storage_pvc_ensure = False
c.JupyterHub.allow_named_servers = True
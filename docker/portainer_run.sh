#!/bin/bash
docker run -d -p 32786:32786 -p 32785:9000 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data -v cert_asus.uglyxu.cn:/cert portainer/portainer --tunnel-port=32786 --ssl --sslcert /cert/1.crt --sslkey /cert/2.key

# dev_sync
Very simple flask application that assists in rapidly resetting the vLab configurations.


Installation:

# must have git installed

[Install Git](https://github.com/git-guides/install-git)


# Must have docker and docker compose installed.
[Install Docker Desktop](https://www.docker.com/products/docker-desktop)

Works well with docker-desktop for macbook

```
Go to you place where you save you git projects, I use /home/user/opt.
Not to be confused with /opt, they are two different thing :-)

% git clone https://github.com/xod442/dev_sync.git
% cd dev_sync
dev_sync%  docker-compose up -d
```
# Gotcha's
Running behind a proxy. You need to add all of the networks that are internal to the no_proxy
in the Dockerfile. Currently it is configured for my labs networks.
Make changes to the Dockerfile before running the docker-compose up.

#Application Notes
Using the application menu, add the credentials of the source IMC servers and the
destination Aruba ClearPass servers. From the pull downs select the source and destination devices and click on the Transfer button.

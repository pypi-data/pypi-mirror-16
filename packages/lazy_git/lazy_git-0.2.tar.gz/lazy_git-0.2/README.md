Lazy Git
========

A streamlined REST API for wrapping access to Git repositories.

Running
-------

*Running*

    python manage.py runserver --host 0.0.0.0 --port 65004

This will run the process locally on port 65004, the `--host 0.0.0.0` is there
so that hosts other than `localhost` can access the service, omit it if this is
not required.

Docker
------

*Building*

    docker build -t lazy_git:latest .

This will build an image based on the official 
[Python 3 Docker image](https://hub.docker.com/_/python/) and defaults to 
setting the `LAZY_GIT_MODE` environment variable to `Production`.

*Running*

    docker run -d -p <local_port>:65004 --name lazy_git -v <local_repo_dir>:/var/lazy_git lazy_git:latest

This command will run a lazy_git process in the background on the port specified
in `<local_port>`.  If you want to override the `LAZY_GIT_MODE` environment
variable (or any other, such as `LAZY_GIT_CONFIG`) then use the
[`-e` argument](https://docs.docker.com/engine/reference/run/#/env-environment-variables).

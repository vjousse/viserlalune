#!/bin/bash
 
NAME="django_vjousse" # Name of the application
DJANGODIR=/home/vjousse/django/envs/vjousse_django/ # Django project directory
SOCKFILE=/home/vjousse/django/envs/vjousse_django/run/gunicorn.sock # we will communicte using this unix socket
USER=vjousse # the user to run as
GROUP=vjousse # the group to run as
NUM_WORKERS=3 # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=project.settings # which settings file should Django use
DJANGO_WSGI_MODULE=project.wsgi # WSGI module name
 
echo "Starting $NAME"
 
# Activate the virtual environment
cd $DJANGODIR
source ./bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$DJANGODIR/project/:$PYTHONPATH
 
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
 
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ./bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--log-level=debug \
--bind=unix:$SOCKFILE
#--bind=127.0.0.1:8080

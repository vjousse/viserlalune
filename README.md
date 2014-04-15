[Mezzanine](http://mezzanine.jupo.org/) based website.

# Installation

I'm using the installation described here: http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/

    pip install -r requirements/project.txt

# Deploy

    fab -A deploy

# South migrations

    ./manage.py schemamigration bestof --auto 
    ./manage.py migrate bestof

    ./manage.py schemamigration bestof --auto --update


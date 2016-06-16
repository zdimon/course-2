##PostgreSQL

###INSTALLING

    apt-get install build-essential postgresql postgresql-contrib

### Creating cluster if it was not created.

    
    pg_createcluster 9.3 main --start

### Remote access

    nano /etc/postgresql/9.3/main/pg_hba.conf


    host all all 0.0.0.0/0 trust


    nano /etc/postgresql/9.3/main/postgresql.conf
    
    listen_addresses = '*'

###Change password for postgres user

    passwd postgres
    sudo -s -u postgres
    psql
    \password postgres


###Restart server

    service postgresql restart

### Install Psycopg

    pip install psycopg2

Psycopg is the most popular PostgreSQL database adapter 
for the Python programming language.

###Django setting

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'pshop',                      # Or path to database file if using sqlite3.
            'USER': 'postgres',                      # Not used with sqlite3.
            'PASSWORD': '1q2w3e',                  # Not used with sqlite3.
            'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        },
        
    }    



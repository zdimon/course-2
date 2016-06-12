##__INIT__

In addition to labeling a directory as a Python package 
and defining __all__, __init__.py allows you to define 
any variable at the package level. 
Doing so is often convenient if a package defines something 
that will be imported frequently, in an API-like fashion. 
This pattern promotes adherence to the Pythonic 
"flat is better than nested" philosophy.

An example

In which I frequently import a sessionmaker called Session 
to interact with my database. 
I wrote a "database" package with a few modules:

database/
    __init__.py
    schema.py
    insertions.py
    queries.py

My __init__.py contains the following code:

    import os

    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine(os.environ['DATABASE_URL'])
    Session = sessionmaker(bind=engine)

Since I define Session here, I can start a new 
session using the syntax below. 
This code would be the same executed from inside or outside 
of the "database" package directory.

    from database import Session
    session = Session()




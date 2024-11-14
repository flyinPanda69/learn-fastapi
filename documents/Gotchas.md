# Gotchas

1) When we anytime send network request to the FastAPI server, its going to go down the list of our path operation and tries to find out the match. And as soon as it finds the first match it starts running that first instance's function


2) Order Matters for path order or routes.
    for eg we are calling /posts/latest
    and we have 2 endpoints as followed

    @app.get('posts/{id}')
    and
    @app.get('posts/latest')

    This will throw error because instead of going to second endpoint it will match the first endpoint
    and try to parse id as string 'latest' which will cause an error.


3) In python application folder is generally considered as package. And a package to work python needs to have a dummy file __init__.py

3) Always hash the password before storing to the db and not as plain text

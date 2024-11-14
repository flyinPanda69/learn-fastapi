# CRUD

## CRUD
- Create: 
    POST
    /posts/
    @app.post("/posts")

    Note: Naming, divide with logic functionalities. Also use plural form (Not post but posts)
- Read:
    GET
    1) /posts/:id
        @app.get("/posts/{id}")
    2) /posts/
        @app.get("/posts")


- Update:
    PUT/PATCH 
    /posts/:id
    @app.put("/posts/{id}")

- Delete:
    DELETE
    /posts/:id
    @app.delete("/posts/{id}")
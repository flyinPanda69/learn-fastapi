# Rough work


my_posts = [{
    "id": 1,
    "title": "Best Hiking Trails in Colorado",
    "content": "Explore these breathtaking trails",
    "published": True,
    "rating": 5
},
{
    "id": 2,
    "title": "Top Museums in New York",
    "content": "Discover the best museums",
    "published": True,
    "rating": 4
},
{
    "id": 3,
    "title": "Famous Landmarks in Paris",
    "content": "Visit these iconic landmarks",
    "published": True,
    "rating": 5
},
{
    "id": 4,
    "title": "Popular Restaurants in Tokyo",
    "content": "Taste the best food in Tokyo",
    "published": True,
    "rating": 4
},
{
    "id": 5,
    "title": "Must-See Attractions in London",
    "content": "Don't miss these attractions",
    "published": True,
    "rating": 5
}
]



def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']== id:
            return i
 


@app.get("/sqlalchemy")
def test_posts( db: Session = Depends(get_db)):
    post = db.query(models.Post).all()
    return {post}

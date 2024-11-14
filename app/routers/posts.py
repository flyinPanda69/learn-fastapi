from typing import List
from fastapi import Response, status, HTTPException, Depends, APIRouter


from sqlalchemy.orm import Session

from app import models
from app.database import get_db

from app.schemas import PostCreate, Post


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get('/', response_model=List[Post])
async def get_posts( db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts""")
    # posts  = cursor.fetchall()

    posts = db.query(models.Post).all()
    return posts



@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Post)
async def create_posts(post: PostCreate, db: Session = Depends(get_db)):
    # cursor.execute( """ INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()
    post.model_dump()
    # new_post = models.Post(title = post.title, content = post.content, published = post.published)
    # below code will remove the headache of model binding manually
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


#id here is called as path parameter
@router.get('/}', response_model=Post)
async def get_post(id: int,  db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts WHERE id = (%s)""", (str(id)))
    # post = cursor.fetchone()
    # print(post)
    print(id)
    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} was not found")
    return post




@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int,  db: Session = Depends(get_db)):
    # deleting post
    # find the index in the array that has required ID
    # my_posts.pop(index)
    
    #index = find_index_post(id)


    # cursor.execute(""" DELETE FROM posts WHERE id = %s returning * """, (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)
    
    # if deleted_post == None:
    if post.first == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} doesnt exists")
    # my_posts.pop(index)

    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{id}', response_model=Post)
async def update_post(id: int, post: PostCreate,  db: Session = Depends(get_db)):

    # cursor.execute(""" UPDATE posts SET title= %s , content= %s, published= %s WHERE id= %s RETURNING * """, (post.title, post.content, post.published,  id))

    # updated_post = cursor.fetchone()
    # print(updated_post)
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post_to_update = post_query.first()

    # index = find_index_post(id)
    if post_to_update == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} doesnt exists")
    
    post_data = post.model_dump(exclude_unset= True) #Use exclude_unset to avoid updating fields that were not provided
    post_query.update(post_data, synchronize_session=False)
    db.commit()
    db.refresh(post_to_update)
    print(post_to_update)
    # post_dict = post.model_dump()
    # post_dict['id'] = id
    # my_posts[index] = post_dict

    return {post_to_update}


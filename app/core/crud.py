from uuid import UUID

from sqlalchemy.orm import Session

from schemas.models import DeletePostResponse, Post, UpdatePost
from schemas.orm import Posts


class Pet:
    def __init__(self, database: Session) -> None:
        self.database: Session = database
        pass

    def create(self, post: Post):
        database_pet = Posts(title=post.title, description=post.description)
        self.database.add(database_pet)
        self.database.commit()
        self.database.refresh(database_pet)
        return database_pet


    def get_all(self):
        return self.database.query(Posts).all()


    def get_one(self, id: UUID):
        return self.database.query(Posts).filter_by(id=id).one()


    def update(self, post: UpdatePost):
        update_query = {Posts.title: post.title, Posts.description: post.description}
        self.database.query(Posts).filter_by(id=post.id).update(update_query)
        self.database.commit()
        return self.database.query(Posts).filter_by(id=post.id).one()


    def delete(self, id: UUID):
        post = self.database.query(Posts).filter_by(id=id).all()
        if not post:
            return DeletePostResponse(detail="Doesnt Exist")
        self.database.query(Posts).filter_by(id=id).delete()
        self.database.commit()
        return DeletePostResponse(detail="Post Deleted")
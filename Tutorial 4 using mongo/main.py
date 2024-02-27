from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from uuid import UUID,uuid4

app=FastAPI()

class Book(BaseModel):
    id:UUID=uuid4()
    title:str=Field(min_length=1,max_length=1000)
    description:str=Field(min_length=1,max_length=1000)
    rating: int= Field(gt=-1, lt=101)

books:[Book]=[]

@app.post('/')
def create_book(book:Book):
    books.append(book)
    return book

@app.get('/')
def get_book_list():
    return books

@app.put('/{book_id}')
def update_book(book_id:UUID,book:Book):
    counter=0
    for i in books:
        counter+=1
        if i.id==book_id:
            books[counter-1]=book
            return books[counter-1]
    raise HTTPException(
        status_code=404,
        detail="book id does not exit"
    )
@app.delete('/{book_id}')
def delete_book(book_id:UUID):
    counter=0
    for i in books:
        counter+=1
        if i.id==book_id:
            b=i
            books.remove(i)
            return {"book":b,"msg":"was deleted successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"book id:{book_id} does not exit"
    )


@app.get('/{book_id}')
def get_a_book(book_id:UUID):
    counter=0
    for i in books:
        counter+=1
        if i.id==book_id:
            return i
    raise HTTPException(
        status_code=404,
        detail=f"book id:{book_id} does not exit"
    )




# @app.get('/{name}')
# async  def name(name:str):
#     return {'user':name}

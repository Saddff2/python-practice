import fastapi

app = fastapi.FastAPI()

my_items = {1:{"name":"test1", "last":"te352"},
            2:{"name":"test2", "last":"te12352"},
            3:{"name":"test35", "last":"t13252"},
            4:{"name":"test1235", "last":"te1235"}}

@app.get('/')
async def root():
    return {"message": "Hello world"}

@app.get('/items')
async def read_item(skip: int = 0, limit: int = 10):
    return list(my_items.items())[skip : skip + limit]

@app.get("/items/{item_id}")
async def hui():
    pass
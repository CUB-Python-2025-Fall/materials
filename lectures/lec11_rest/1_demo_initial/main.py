from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_index():
	return 'hello'


@app.get("/posts")
async def get_posts():
    return {"posts": ["Hello world!", "Some other post"]}
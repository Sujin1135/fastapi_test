import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from applications import router
app = FastAPI(
    title='fast-api',
    description='test fast-api by mango',
    docs_url='/docs',
    redoc_url='/redoc',
    version='0.0.1'
)


app.include_router(router, prefix='/api/v1')

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=['*'],
    allow_headers=['*']
)

if __name__ == '__main__':
    uvicorn.run(app)

from fastapi import FastAPI, HTTPException
import uvicorn


app = FastAPI(
    title="{{cookiecutter.project_name}}",
    version="1.0",
    description="{{cookiecutter.short_description}}"
)


@app.on_event('startup')
async def init():
    '''
    Initialize ML models
    '''
    pass


@app.get('/')
async def health_check():
    return {
        'success': True,
        'message': 'Welcome to {{cookiecutter.project_name}} API'
    }


@app.post('/predict')
async def predict():
    return {
        'success': True
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=5000)

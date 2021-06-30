import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.param_functions import Depends

from settings import APISettings

from .api_models import FormRequestModel, JsonRequestModel

app = FastAPI(
    title="{{cookiecutter.project_name}}",
    version="1.0",
    description="{{cookiecutter.short_description}}",
)
config = APISettings()


@app.on_event("startup")
async def init():
    """
    Initialize ML models
    """
    # How to use app settings to load model
    # model = load_model(config.MODEL_DIR)
    pass


@app.get("/")
async def health_check():
    return {"success": True, "message": "Welcome to {{cookiecutter.project_name}} API"}


@app.post("/predictJson")
async def predict_json(json_req: JsonRequestModel):
    return {"success": True}


@app.post("/predictForm")
async def predict_form(form_req: FormRequestModel = Depends(FormRequestModel)):
    return {"success": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=5000)

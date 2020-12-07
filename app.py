from fastapi import FastAPI
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from joblib import load

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
async def home(request: Request):
    result = ""
    
    if request.method == "POST": 
        form = await request.form()
        if form["height"] and form["weight"]: 
            height =  form["height"]
            weight =  form["weight"]
            result = predict(int(height), int(weight))
    return templates.TemplateResponse("index.html", {"request": request, "result":result})



# @app.route("predict")
def predict(a, b): 
    clf = load('gender_model.joblib') 

    prediction = clf.predict([(a, b)])

    if prediction[0]:
        result = "Male"
    else:
        result = "Female"
        
        
    return result

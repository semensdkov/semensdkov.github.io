from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="EcoSuds")

app.mount("/static", StaticFiles(directory="/"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse({"request": request}, "index.html")


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse({"request": request}, "dashboard.html")

@app.get("/process", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse({"request": request}, "process.html")

@app.get("/account", response_class=HTMLResponse)
async def account_page(request: Request):
    return templates.TemplateResponse({"request": request}, "account.html")

@app.post("/submit-oil", response_class=HTMLResponse)
async def submit_oil(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    quantity: str = Form(...),
    address: str = Form(...),
    notes: str = Form(""),
):
    print(f"📬 New pickup request: {name} / {email} / {quantity}L")
    return """
    <div class="success-msg show">
        <i class="fa-solid fa-circle-check"></i>
        <h3>Thank you!</h3>
        <p>We've received your request. Our team will contact you shortly.</p>
    </div>
    """

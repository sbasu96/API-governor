import json
import yaml
import tempfile

from fastapi import APIRouter, Request, UploadFile, File, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from api_governor.core.loader import load_spec_from_content
from api_governor.core.validator import validate_structure
from api_governor.core.rule_engine import run_rules
from api_governor.core.semantic_analyzer import run_semantic_analysis


router = APIRouter()
templates = Jinja2Templates(directory="src/api_governor/web/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/analyze", response_class=HTMLResponse)
async def analyze(
    request: Request,
    file: UploadFile = File(...),
    ai_enabled: bool = Form(False)
):
    content = await file.read()
    spec = load_spec_from_content(content, file.filename)

    structural_errors = validate_structure(spec)
    lint_errors = run_rules(spec)
    semantic_findings = run_semantic_analysis(spec)

    result = {
        "structural_errors": structural_errors,
        "lint_errors": lint_errors,
        "semantic_findings": semantic_findings
    }

    return templates.TemplateResponse(
        "results.html",
            {
                "request": request,
                "structural_errors": structural_errors,
                "lint_errors": lint_errors,
                "semantic_findings": semantic_findings
            }
    )
from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class LintIssue(BaseModel):
    rule: str
    path: str
    method: str
    message: str
    severity: str = "error"


class StructuralIssue(BaseModel):
    message: str
    severity: str = "error"


class AIIssue(BaseModel):
    problem: str
    reason: str
    suggested_fix: str
    severity: str = "warning"


class PathAIResult(BaseModel):
    path: str
    issues: List[AIIssue]


class AnalysisReport(BaseModel):
    structural_errors: List[StructuralIssue]
    lint_errors: List[LintIssue]
    ai_findings: Optional[List[PathAIResult]] = []

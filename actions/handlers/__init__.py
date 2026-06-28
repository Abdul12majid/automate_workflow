from .extract import ExtractHandler
from .email import EmailHandler
from .report import ReportHandler
from .http import HTTPRequestHandler
from .ai_extract import AIExtractHandler


HANDLERS = {
    "extract_data": ExtractHandler(),
    "send_email": EmailHandler(),
    "generate_report": ReportHandler(),
    "http_request": HTTPRequestHandler(),
    "ai_extract": AIExtractHandler(),
}
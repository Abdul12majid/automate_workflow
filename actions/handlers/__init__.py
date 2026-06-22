from .extract import ExtractHandler
from .email import EmailHandler
from .report import ReportHandler


HANDLERS = {
    "extract_data": ExtractHandler(),
    "send_email": EmailHandler(),
    "generate_report": ReportHandler(),
}
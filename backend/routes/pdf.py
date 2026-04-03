import tempfile
from fastapi import APIRouter, UploadFile
import tempfile
from tools import load_pdf

router = APIRouter()


@router.post("/upload")
def upload_pdf(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(file.file.read())
        temp_path = temp_file.name

    load_pdf.invoke({"file_path": temp_path})

from pypdf.errors import PdfStreamError
import tempfile
from fastapi import APIRouter, UploadFile, HTTPException
import tempfile
from tools import load_pdf

router = APIRouter()


@router.post("/upload")
def upload_pdf(file: UploadFile):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(file.file.read())
            temp_path = temp_file.name
            load_pdf.invoke({"file_path": temp_path})
        return {"status_code": 200, "message": "PDF uploaded successfully"}
    except PdfStreamError as e:
        raise HTTPException(status_code=400, detail="Please upload a valid pdf file")
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error while uploading pdf")

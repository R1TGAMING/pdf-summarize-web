from langchain.tools import tool
from pypdf import PdfReader


@tool
def load_pdf(file_path: str) -> str:
    """load the pdf file and return the text"""

    reader = PdfReader(file_path)
    num_of_pages = len(reader.pages)
    text = ""
    if num_of_pages == 1:
        text = reader.pages[0].extract_text()
    else:
        for page in reader.pages:
            text += page.extract_text()
    return text


@tool
def summarize_pdf(text: str) -> str:
    """summarize the text"""

    return text

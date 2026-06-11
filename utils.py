import os
import fitz

from PIL import Image
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()

client = Mistral(
    api_key=os.getenv("MISTRAL_API_KEY")
)


def extract_text_from_pdf(uploaded_pdf):

    text = ""

    pdf_document = fitz.open(
        stream=uploaded_pdf.read(),
        filetype="pdf"
    )

    for page in pdf_document:
        text += page.get_text()

    return text


def extract_text_from_image(uploaded_image):

    temp_path = "temp_image.png"

    image = Image.open(uploaded_image)

    image.save(temp_path)

    uploaded_file = client.files.upload(
        file={
            "file_name": "event_image.png",
            "content": open(temp_path, "rb")
        },
        purpose="ocr"
    )

    signed_url = client.files.get_signed_url(
        file_id=uploaded_file.id
    )

    ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "image_url",
            "image_url": signed_url.url
        }
    )

    extracted_text = ""

    for page in ocr_response.pages:
        extracted_text += page.markdown

    return extracted_text
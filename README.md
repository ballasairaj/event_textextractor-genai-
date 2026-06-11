# 🎯 Event Information Extractor using Mistral AI

## 📌 Overview

Event announcements are often shared as posters, flyers, emails, PDFs, social media posts, and promotional banners. Extracting important information manually from these documents can be time-consuming and error-prone.

This project is an AI-powered Event Information Extractor that automatically identifies and extracts key event details from:

* Plain Text
* Event Posters (Images)
* Event PDFs

The extracted information is returned in a structured JSON format using Mistral AI and OCR technology.

---

## 🚀 Features

### ✅ Text-Based Event Extraction

Users can directly paste an event description, and the system extracts:

* Event Name
* Event Date
* Event Time
* Event Location
* Organizer

---

### ✅ Image-Based Event Extraction

Upload event posters in:

* JPG
* JPEG
* PNG

The system:

1. Performs OCR on the image.
2. Extracts textual content.
3. Uses Mistral AI to identify event details.
4. Returns structured JSON output.

---

### ✅ PDF-Based Event Extraction

Upload event brochures, flyers, or promotional PDFs.

The system:

1. Extracts text from PDFs.
2. Processes extracted content through Mistral AI.
3. Generates structured event information.

---

### ✅ Smart Missing Value Handling

The model never invents information.

If a field is unavailable:

```json
{
  "organizer": "not_available"
}
```

This ensures reliable and trustworthy extraction.

---

### ✅ Attractive Streamlit Interface

* Modern UI
* Image Preview
* JSON Viewer
* OCR Output Viewer
* Sidebar Navigation
* Responsive Layout

---

## 🏗️ Project Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ├── Text Input
 ├── Image Upload
 └── PDF Upload
 │
 ▼
Document Processing Layer
 │
 ├── PDF Text Extraction
 └── OCR Processing
 │
 ▼
Prompt Engineering Layer
 │
 ▼
Mistral AI
 │
 ▼
JSON Validation Layer
 │
 ▼
Structured Event Output
```

---

## 📂 Project Structure

```text
event-information-extractor/
│
├── app.py
├── utils.py
├── llm_service.py
├── prompt_template.py
│
├── requirements.txt
├── .env
├── .gitignore
│
└── README.md
```

---

## 🧠 Technologies Used

### Frontend

* Streamlit

### LLM

* Mistral Small Latest

### OCR

* Mistral OCR

### Document Processing

* PyMuPDF

### Image Processing

* Pillow

### Environment Management

* Python Dotenv

---

## ⚙️ Installation


### Create Virtual Environment

Windows

```bash
py -3.11 -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3.11 -m venv venv

source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

## 📥 Input Types

### 1. Text Input

Example:

```text
Join us for the AI Conference on July 10 at 10 AM in Hyderabad, hosted by TechNova.
```

Output:

```json
{
  "event_name": "AI Conference",
  "event_date": "July 10",
  "event_time": "10 AM",
  "event_location": "Hyderabad",
  "organizer": "TechNova"
}
```

---

### 2. Image Input

Upload:

* Event Posters
* Hiring Posters
* Conference Flyers
* Workshop Invitations

Supported Formats:

```text
jpg
jpeg
png
```

---

### 3. PDF Input

Upload:

* Event Brochures
* Conference Schedules
* Promotional Flyers

Supported Format:

```text
pdf
```

---

## 🎯 Output Schema

```json
{
  "event_name": "string",
  "event_date": "string",
  "event_time": "string",
  "event_location": "string",
  "organizer": "string"
}
```

---

## 🧩 Prompt Engineering

The project uses a structured extraction prompt with the following rules:

* No hallucination
* JSON-only responses
* Missing values → "not_available"
* Strong organizer identification
* Event title prioritization
* OCR-aware extraction

---

## 🔍 Workflow

### Text Input Workflow

```text
Text
 │
 ▼
Mistral AI
 │
 ▼
JSON Output
```

---

### Image Input Workflow

```text
Image
 │
 ▼
OCR
 │
 ▼
Extracted Text
 │
 ▼
Mistral AI
 │
 ▼
JSON Output
```

---

### PDF Input Workflow

```text
PDF
 │
 ▼
Text Extraction
 │
 ▼
Mistral AI
 │
 ▼
JSON Output
```

## 🌟 Future Enhancements

* Multi-event extraction from a single document
* Event calendar (.ics) generation
* Google Calendar integration
* Event categorization
* Venue geolocation mapping
* Event summary generation
* QR code extraction
* Multilingual support

---

## 👨‍💻 Author

**Sairaj Balla**

AI/ML Engineer | Generative AI Developer

### Skills

* Machine Learning
* Deep Learning
* Computer Vision
* Generative AI
* Large Language Models
* OCR Systems
* Streamlit Applications

---

## 📜 License

This project is developed for educational and portfolio purposes.

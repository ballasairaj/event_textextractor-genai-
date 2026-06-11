import streamlit as st

from utils import (
    extract_text_from_pdf,
    extract_text_from_image
)

from llm_service import (
    extract_event_info
)

st.set_page_config(
    page_title="Event Information Extractor",
    page_icon="🎯",
    layout="wide"
)

st.markdown("""
<style>

.main-title{
text-align:center;
font-size:45px;
font-weight:bold;
color:#4F46E5;
}

.sub-title{
text-align:center;
color:gray;
margin-bottom:20px;
}

.output-box{
padding:10px;
border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='main-title'>🎯 Event Information Extractor</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Extract Event Information from Text, Images and PDFs using Mistral AI</div>",
    unsafe_allow_html=True
)

st.divider()

with st.sidebar:

    st.header("Input Source")

    input_type = st.radio(
        "Choose Input Type",
        [
            "Text",
            "Image",
            "PDF"
        ]
    )

# TEXT INPUT

if input_type == "Text":

    text = st.text_area(
        "Enter Event Description",
        height=250
    )

    if st.button("Extract Details"):

        with st.spinner("Analyzing Event..."):

            result = extract_event_info(text)

        st.json(result)

# IMAGE INPUT

elif input_type == "Image":

    image = st.file_uploader(
        "Upload Event Poster",
        type=["jpg", "jpeg", "png"]
    )

    if image:
        col1, col2, col3 = st.columns([1,2,1])

        with col2:
            st.image(
                image,
                width=300
            )

       

        if st.button("Extract Details"):

            with st.spinner("Reading Event Poster..."):

                extracted_text = extract_text_from_image(
                    image
                )

                result = extract_event_info(
                    extracted_text
                )

            st.json(result)

            with st.expander("OCR Output"):
                st.write(extracted_text)

# PDF INPUT

elif input_type == "PDF":

    pdf = st.file_uploader(
        "Upload Event PDF",
        type=["pdf"]
    )

    if pdf:

        if st.button("Extract Details"):

            with st.spinner("Reading PDF..."):

                extracted_text = extract_text_from_pdf(
                    pdf
                )

                result = extract_event_info(
                    extracted_text
                )

            st.json(result)

            with st.expander("Extracted Text"):
                st.write(extracted_text)

st.divider()

st.caption(
    "Powered by Mistral AI + OCR + Streamlit"
)
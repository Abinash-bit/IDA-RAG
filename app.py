import streamlit as st
from question_answering import query_docs
 
st.title("Document Q&A Application")
 
# Initialize session state for question
if 'question' not in st.session_state:
    st.session_state.question = ""
 
# Example questions dropdown
example_questions = [
    "Select an example question...",
    "Summarize the project Kickoff",
    "Brief the CO2 emissions in Australia",
    "Tell about hyundai sales report in Mumbai",
    "Explain about the Speech recognition PPT made by Abinash.",
    "Give me the last email sent to rachit, with its body.",
]
 
selected_example = st.selectbox("Example Questions", example_questions)
 
# Update session state if an example is selected
if selected_example != example_questions[0]:
    st.session_state.question = selected_example
 
# Text input for question
question = st.text_input(
    "Ask a question about the documents:",
    value=st.session_state.question
)
 
def format_answer(answer: str) -> str:
    """Format the answer text with proper line breaks"""
    return answer
 
if st.button("Get Answer") and question.strip():
    answer, sources, confidences = query_docs(question)
    
    # Display answer with proper formatting
    st.subheader("Answer:")
    st.markdown(format_answer(answer))
 
    # Add "Go to Source" button for the first available source
    first_valid_source = next((src for src in sources if src != "Link not available"), None)
    if first_valid_source:
        st.markdown(
            f"""
            <a href="{first_valid_source}" target="_blank">
                <button style="background-color:#0d47a1;color:white;padding:0.5rem 1rem;border:none;border-radius:4px;cursor:pointer;">
                    Go to Source
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )
 
    # Display sources with clickable links
    st.subheader("Document Sources:")
    for i, (src, score) in enumerate(zip(sources, confidences), start=1):
        if src != "Link not available":
            st.markdown(
                f"""
                <div style="margin-bottom: 1rem; padding: 0.5rem; border-left: 4px solid #0d47a1;">
                    <strong>Source {i}</strong> (Confidence: {(1 - score):.2f})<br>
                    <a href="{src}" target="_blank" style="word-break: break-all; color: #0d47a1; text-decoration: none;">
                        {src}
                    </a>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.warning(f"Source {i} link unavailable (Confidence: {score:.2f})")
 
# Add styling
st.markdown("""
    <style>
        div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlock"] {
            margin-top: 1.5rem;
        }
        a:hover {
            text-decoration: underline !important;
        }
    </style>
""", unsafe_allow_html=True)

from google import genai
import chromadb # type: ignore
from generate_embeddings import get_embedding
 
PROJECT_ID = "boxwood-theory-450601-g5"
LOCATION = "us-central1"
MODEL_ID = "gemini-2.5-pro-preview-03-25"
 
genai_client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
chat = genai_client.chats.create(model=MODEL_ID)
 
client = chromadb.PersistentClient(path="chroma_store")
collection = client.get_or_create_collection(name="qa_documents")
 
# /home/zclap/production/QA_LLM/data/docx/Meeting_Minutes_0.docx
 
 
values = {
    "home/zclap/production/QA_LLM/data/docx/Meeting_Minutes_0.docx" : "https://zclapinc-my.sharepoint.com/:w:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7BB3ADEB1E-0D64-4C9D-BEA7-6FC1DD2B57AB%7D&file=Meeting_Minutes_0.docx&action=default&mobileredirect=true",
    "home/zclap/production/QA_LLM/data/docx/creative_writing_sample.docx" : "https://zclapinc-my.sharepoint.com/:w:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7B3A7BB2F2-6F28-49C0-A922-B8D1FA709833%7D&file=creative_writing_sample.docx&action=default&mobileredirect=true",
    "home/zclap/production/QA_LLM/data/docx/sample_document.docx" : "https://zclapinc-my.sharepoint.com/:w:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7B7D80A9BD-784B-4032-AED6-1A5F94C4C72B%7D&file=sample_document.docx&action=default&mobileredirect=true",
    "home/zclap/production/QA_LLM/data/docx/Australia.docx" :"https://zclapinc-my.sharepoint.com/:w:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7B0C2B0071-A34C-4F72-94EC-D2F910CF1297%7D&file=Australia.docx&action=default&mobileredirect=true&wdOrigin=OUTLOOK-METAOS.FILEBROWSER",
    "home/zclap/production/QA_LLM/data/docx/Coral Reefs.docx" : "https://zclapinc-my.sharepoint.com/:w:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7BFF65BE22-28BF-48A1-96D8-2B810722897A%7D&file=Coral%20Reefs.docx&action=default&mobileredirect=true&wdOrigin=OUTLOOK-METAOS.FILEBROWSER",
    "home/zclap/production/QA_LLM/data/pptx/QBR_Presentation_0.pptx" : "https://zclapinc-my.sharepoint.com/:p:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7B732E5569-16A1-4E73-BA43-D4515B2F6DCB%7D&file=QBR_Presentation_0.pptx&action=edit&mobileredirect=true",
    "home/zclap/production/QA_LLM/data/pptx/QBR_Presentation_1.pptx" : "https://zclapinc-my.sharepoint.com/:p:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7B94FAACAF-0D4B-43F1-A751-D1EC3CCBA319%7D&file=QBR_Presentation_1.pptx&action=edit&mobileredirect=true",
    "home/zclap/production/QA_LLM/data/pptx/QBR_Presentation_2.pptx" : "https://zclapinc-my.sharepoint.com/:p:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7B239D6F2B-91D7-41F3-953F-5413F4A59A17%7D&file=QBR_Presentation_2.pptx&action=edit&mobileredirect=true",
    "home/zclap/production/QA_LLM/data/pptx/Photosynthesis-Powering-Life-on-Earth.pptx" : "https://zclapinc-my.sharepoint.com/:p:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7B68AC22DA-7997-41CC-AF0E-8F72DE3404DC%7D&file=Photosynthesis-Powering-Life-on-Earth.pptx&action=edit&mobileredirect=true&wdOrigin=OUTLOOK-METAOS.FILEBROWSER",
    "home/zclap/production/QA_LLM/data/pptx/Introduction-to-Speech-Recognition.pptx" : "https://zclapinc-my.sharepoint.com/:p:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7B06433A9F-E789-49D4-9EA0-AD45DA28DF39%7D&file=Introduction-to-Speech-Recognition.pptx&action=edit&mobileredirect=true&wdOrigin=OUTLOOK-METAOS.FILEBROWSER",
    "home/zclap/production/QA_LLM/data/pptx/Street-Art-Transforming-Urban-Spaces.pptx" : "https://zclapinc-my.sharepoint.com/:p:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7B15FFC69A-76E7-46B8-A58F-CB17E078C5BA%7D&file=Street-Art-Transforming-Urban-Spaces.pptx&action=edit&mobileredirect=true&wdOrigin=OUTLOOK-METAOS.FILEBROWSER",
    "home/zclap/production/QA_LLM/data/pptx/The-AI-Revolution-in-Healthcare.pptx" : "https://zclapinc-my.sharepoint.com/:p:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7BF715069E-3F5A-4483-B32A-6094179209BF%7D&file=The-AI-Revolution-in-Healthcare.pptx&action=edit&mobileredirect=true&wdOrigin=OUTLOOK-METAOS.FILEBROWSER",
    "home/zclap/production/QA_LLM/data/pptx/The-Unseen-Architect-Unveiling-the-Role-of-Dark-Matter.pptx" : "https://zclapinc-my.sharepoint.com/:p:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7BAFD55DC5-3416-4222-8747-6F0E5EB13EDF%7D&file=The-Unseen-Architect-Unveiling-the-Role-of-Dark-Matter.pptx&action=edit&mobileredirect=true&wdOrigin=OUTLOOK-METAOS.FILEBROWSER",
    "home/zclap/production/QA_LLM/data/pptx/Your-Company-Name-Transforming-Client-Company-Names-Business.pptx" : "https://zclapinc-my.sharepoint.com/:p:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7BECF30CB8-0739-4B7C-A0C5-6F432EC863EA%7D&file=Your-Company-Name-Transforming-Client-Company-Names-Business.pptx&action=edit&mobileredirect=true&wdOrigin=OUTLOOK-METAOS.FILEBROWSER",
    "home/zclap/production/QA_LLM/data/excel/Sales_Report_0.xlsx" : "https://zclapinc-my.sharepoint.com/:x:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7B0330D209-9940-49D4-BA36-F790CCBB0891%7D&file=Sales_Report_0.xlsx&action=default&mobileredirect=true",
    "home/zclap/production/QA_LLM/data/excel/Sales_Report_1.xlsx" : "https://zclapinc-my.sharepoint.com/:x:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7B34046B84-02A9-41B5-B93E-53E1DA8B0A4A%7D&file=Sales_Report_1.xlsx&action=default&mobileredirect=true",
    "home/zclap/production/QA_LLM/data/excel/Sales_Report_2.xlsx" : "https://zclapinc-my.sharepoint.com/:x:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7BB1030482-3499-41E7-BEAF-A9508903BA17%7D&file=Sales_Report_2.xlsx&action=default&mobileredirect=true",
    "home/zclap/production/QA_LLM/data/excel/CO2_Emissions_Data.xlsx" : "https://zclapinc-my.sharepoint.com/:x:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7BF2C56A5F-457F-4732-8A26-844BE08FBF14%7D&file=CO2_Emissions_Data.xlsx&action=default&mobileredirect=true&wdOrigin=OUTLOOK-METAOS.FILEBROWSER",
    "home/zclap/production/QA_LLM/data/excel/hyundai_car_sales.xlsx" : "https://zclapinc-my.sharepoint.com/:x:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7B1EBEDBA7-F95F-44D9-97B7-51D697D98F2C%7D&file=hyundai_car_sales.xlsx&action=default&mobileredirect=true&wdOrigin=OUTLOOK-METAOS.FILEBROWSER",
    "home/zclap/production/QA_LLM/data/excel/Population_Health_Metrics.xlsx" : "https://zclapinc-my.sharepoint.com/:x:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7BDD27F078-B162-4C67-8E4A-697F314D9A36%7D&file=Population_Health_Metrics.xlsx&action=default&mobileredirect=true&wdOrigin=OUTLOOK-METAOS.FILEBROWSER",
    "home/zclap/production/QA_LLM/data/excel/Renewable_Energy_Stats.xlsx" : "https://zclapinc-my.sharepoint.com/:x:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7B6C294C30-E3F3-44AC-A39A-C1F463DE568D%7D&file=Renewable_Energy_Stats.xlsx&action=default&mobileredirect=true&wdOrigin=OUTLOOK-METAOS.FILEBROWSER",
    "home/zclap/production/QA_LLM/data/excel/Tech_Company_Financials.xlsx" : "https://zclapinc-my.sharepoint.com/:x:/r/personal/abinash_mahapatra_zclap_com/_layouts/15/Doc.aspx?sourcedoc=%7BEA31AC73-033F-47AD-9A7E-670C79902170%7D&file=Tech_Company_Financials.xlsx&action=default&mobileredirect=true&wdOrigin=OUTLOOK-METAOS.FILEBROWSER",
    "home/zclap/production/QA_LLM/data/email/outlook.msg" : "https://zclapinc-my.sharepoint.com/:u:/g/personal/abinash_mahapatra_zclap_com/EXW7fuN3XZNMoz1vUCoajEkBbuJqh03WctHLFR5bVFrnOg?e=kclAPR",
    "home/zclap/production/QA_LLM/data/email/City letter simulation — round 3 test.msg" : "https://zclapinc-my.sharepoint.com/my?ga=1&id=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail%2FCity%20letter%20simulation%20%E2%80%94%20round%203%20test%2Emsg&parent=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail",
    "home/zclap/production/QA_LLM/data/email/Random memo for scanning experiment.msg" : "https://zclapinc-my.sharepoint.com/my?ga=1&id=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail%2FRandom%20memo%20for%20scanning%20experiment%2Emsg&parent=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail",
    "home/zclap/production/QA_LLM/data/email/Apology for Missing the _Client Strategy Sync-Up_ Meeting.msg" : "https://zclapinc-my.sharepoint.com/my?id=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail%2FApology%20for%20Missing%20the%20%5FClient%20Strategy%20Sync%2DUp%5F%20Meeting%2Emsg&parent=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail",
    "home/zclap/production/QA_LLM/data/email/Product Inquiry_ Custom Eco-Printed Cloth Bags for Bulk Order.msg" : "https://zclapinc-my.sharepoint.com/my?id=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail%2FProduct%20Inquiry%5F%20Custom%20Eco%2DPrinted%20Cloth%20Bags%20for%20Bulk%20Order%2Emsg&parent=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail",
    "home/zclap/production/QA_LLM/data/email/Request for Extension on Essay for _Modern Indian Literature_ Course.msg" : "https://zclapinc-my.sharepoint.com/my?id=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail%2FRequest%20for%20Extension%20on%20Essay%20for%20%5FModern%20Indian%20Literature%5F%20Course%2Emsg&parent=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail",
    "home/zclap/production/QA_LLM/data/email/Request for Meeting to Review _Q2 Marketing Campaign_ Progress.msg" : "https://zclapinc-my.sharepoint.com/my?id=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail%2FRequest%20for%20Meeting%20to%20Review%20%5FQ2%20Marketing%20Campaign%5F%20Progress%2Emsg&parent=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail",
    "home/zclap/production/QA_LLM/data/email/Thank You for Your Help at the _Spring Charity Gala_.msg" : "https://zclapinc-my.sharepoint.com/my?ga=1&id=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail%2FThank%20You%20for%20Your%20Help%20at%20the%20%5FSpring%20Charity%20Gala%5F%2Emsg&parent=%2Fpersonal%2Fabinash%5Fmahapatra%5Fzclap%5Fcom%2FDocuments%2Fdata%2Femail"
}
 
# def normalize_path(path: str) -> str:
#     """Standardize paths to forward slashes for consistent lookups"""
#     return path.replace("\\", "/")
 
def normalize_path(path: str) -> str:
    """Standardize paths for consistent lookups"""
    path = path.replace("\\", "/").strip()  # Add .strip() here
    if path.startswith("/"):
        path = path[1:]
    return path
 
def query_docs(user_question: str, top_k: int = 1):
    query_embedding = get_embedding(user_question)
    if not query_embedding:
        return "Couldn't embed the question.", [], []
    
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    retrieved_docs = results["documents"][0]
    sources = results["metadatas"][0]
    distances = results["distances"][0]
    
    # Replace local paths with online links
    online_sources = []
    for src in sources:
        raw_path = src["source"]
        normalized_path = normalize_path(raw_path)
        online_sources.append(values.get(normalized_path, "Link not available"))  # Never show local path
        
    max_distance = max(distances) if distances else 1
    confidences = [1 - (d / max_distance) for d in distances]
 
    # context = "\n---\n".join([
    #     f"{doc}\n[Source: {src}]"
    #     for doc, src in zip(retrieved_docs, online_sources)
    # ])
 
    context = "\n---\n".join([
        f"{doc}\n[Source: {src}]\n"
        f"Subject: {meta.get('subject', 'N/A')}\nDate: {meta.get('sent_date', 'N/A')}"
        for doc, src, meta in zip(retrieved_docs, online_sources, sources)
    ])
    
    prompt = f"""Answer the question based on these context excerpts.
 
    When using information from documents:
    1. Provide your answer
    
 
    context:\n{context}\n\nQuestion: {user_question}"""
    
    response = chat.send_message(prompt)
    print(normalized_path)
    print("Dictionary keys:", [k for k in values.keys() if k in normalized_path])
    return response.text, online_sources, confidences
 
if __name__ == "__main__":
    while True:
        question = input("\nAsk a question (or type 'exit'): ")
        if question.lower() == 'exit':
            break
        answer, sources, confidences= query_docs(question)
        print("\nAnswer:", answer)
        print("\nCited Sources:")
        for src, score in zip(sources, confidences):
            print(f"- {src} (Confidence: {score:.2f})")
        print("\nDistances:")

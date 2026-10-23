from parse_input import parse_query
from pydantic import BaseModel
import pandas as df
from structure_data import apply_spec 
from generate_answer import generate_response 
from rag_data import rag 
from render_markdown import markdown_to_text
from fastapi import FastAPI

app=FastAPI()
class question(BaseModel):
    query:str

@app.post("/api/")
def generatar(qns:question):
    path="AcmeFlow_Synthetic_Product_Catalog.xlsx"
    Text="find product with id PRD-0003 VAR-00029 HK02022-V03 REV-00028"
    Product_IDs=df.read_excel(path,sheet_name="Products")
    Variant_IDs=df.read_excel(path,sheet_name="Variants")
    Review_IDs=df.read_excel(path,sheet_name="Reviews")
    sheets = {"Products": Product_IDs, "Variants": Variant_IDs, "Reviews": Review_IDs}


    json_query=parse_query(qns.query)
    print(json_query)
    result=[]
    

    if json_query["route"] =="structured":
        structure_result=apply_spec(sheets,json_query["query"])
        result.append(structure_result)
        print(structure_result)
   
    elif json_query["route"]=="rag":
        rag_result=rag(qns.query)
        result.append(rag_result)
       
    elif json_query["route"]=="hybrid":
        structure_result=apply_spec(sheets,json_query)
        rag_result=rag(qns.query)
        result.append(structure_result)
        result.append(rag_result)
      
   

    answer= generate_response(qns.query,result,json_query["route"])
    return(markdown_to_text(answer))
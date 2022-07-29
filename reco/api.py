from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List, Tuple

from .model import get_model, Model

app = FastAPI()


class RecoRequest(BaseModel):
    product_id: str


class RecoResponse(BaseModel):
    recos: List[List]
# Senaryo2: RecoResponse class'i yoruma alinir.

@app.post("/predict", response_model=RecoResponse)
# Senaryo2: response_model = List[Tuple[str,float]] seklinde verilir. Return reco yapilir.
def predict(request: RecoRequest, model: Model = Depends(get_model)):
    reco = model.predict(request.product_id)
    return RecoResponse(
        recos=reco
    )

## DIGER CALISAN YOL ##

"""
class RecoResponse silinir.

@app.post("/predict", response_model=List[Tuple[str,float]]) 
def predict(request: RecoRequest, model: Model = Depends(get_model)):
    reco = model.predict(request.product_id)
    return reco
"""

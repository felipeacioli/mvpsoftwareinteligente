from pydantic import BaseModel
from typing import Optional, List
from model.amostra import Amostra
import json
import numpy as np

class AmostraSchema(BaseModel):
    """ Define como uma nova amostra analisada deve ser representada
    """    
    ph: float = 5.45
    hardness: float = 181.34
    solids: float = 1551.54
    chloramines: float = 7.85
    sulfate: float = 315.54
    conductivity: float = 283.25
    organic_carbon: float = 14.85
    trihalomethanes: float = 69.23
    turbidity: float = 3.58
    
    
class AmostraViewSchema(BaseModel):
    """Define como a análise de uma amostra será retornada
    """

    id: int = 1
    ph: float = 5.45
    hardness: float = 181.34
    solids: float = 1551.54
    chloramines: float = 7.85
    sulfate: float = 315.54
    conductivity: float = 283.25
    organic_carbon: float = 14.85
    trihalomethanes: float = 69.23
    turbidity: float = 3.58
    outcome: int = None
    
    
class AmostraBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no id  da amostra.
    """
    id: int = 1

class ListaAmostrasSchema(BaseModel):
    """Define como uma lista de análises será representada
    """
    amostras: List[AmostraSchema]

    
class AmostraDelSchema(BaseModel):
    """Define como uma análise para deleção será representada
    """
    id: int = 1
    
# Apresenta apenas os dados de uma amostra    
def apresenta_amostra(amostra: Amostra):
    """ Retorna uma representação da amostra seguindo o schema definido em
        AmostraViewSchema.
    """
    return {

        "id": amostra.id,
        "ph": amostra.ph,
        "hardness": amostra.hardness,
        "solids": amostra.solids,
        "chloramines": amostra.chloramines,
        "sulfate": amostra.sulfate,
        "conductivity": amostra.conductivity,
        "organic_carbon": amostra.organic_carbon,
        "trihalomethanes": amostra.trihalomethanes,
        "turbidity": amostra.turbidity,
        "outcome": amostra.outcome

    }
    
# Apresenta uma lista de pacientes
def apresenta_amostras(amostras: List[Amostra]):
    """ Retorna uma representação da amostra seguindo o schema definido em
        AmostraViewSchema.
    """
    result = []
    for amostra in amostras:
        result.append({
        
        "id": amostra.id,
        "ph": amostra.ph,
        "hardness": amostra.hardness,
        "solids": amostra.solids,
        "chloramines": amostra.chloramines,
        "sulfate": amostra.sulfate,
        "conductivity": amostra.conductivity,
        "organic_carbon": amostra.organic_carbon,
        "trihalomethanes": amostra.trihalomethanes,
        "turbidity": amostra.turbidity,
        "outcome": amostra.outcome

        })

    return {"amostras": result}


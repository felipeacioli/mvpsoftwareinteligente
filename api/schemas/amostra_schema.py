from pydantic import BaseModel
from typing import Optional, List
from model.amostra import Amostra
import json
import numpy as np

class AmostraSchema(BaseModel):
    """ Define como uma nova amostra a ser inserida deve ser representada
    """
    numero: int = 10
    ph: float = 8.316766
    hardness: float = 181.101509
    solids: float = 28748.687739
    chloramines: float = 7.513408
    sulfate: float = 303.309771
    conductivity: float = 363.266516
    organic_carbon: float = 11.558279
    trihalomethanes: float = 54.917862
    turbidity: float = 2.672989  
    
class AmostraViewSchema(BaseModel):
    """Define como uma amsotra será retornado
    """
    id: int = 1
    numero: int = 10
    ph: float = 8.316766
    hardness: float = 181.101509
    solids: float = 28748.687739
    chloramines: float = 7.513408
    sulfate: float = 303.309771
    conductivity: float = 363.266516
    organic_carbon: float = 11.558279
    trihalomethanes: float = 54.917862
    turbidity: float = 2.672989
    outcome: int = None
    
class AmostraBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no número da amostra.
    """
    numero: int = 10

class ListaAmostraSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    amostras: List[AmostraSchema]

    
class AmostraDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    numero: int = 10

# Apresenta apenas os dados de uma amostra    

def apresenta_amostra(amostra: Amostra):
    """ Retorna uma representação da amostra seguindo o schema definido em
        AmostraViewSchema.
    """
    return {
        
        "id": amostra.id,
        "numero": amostra.numero,
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
    
# Apresenta uma lista de amostras
def apresenta_amostras(amostras: List[Amostra]):
    """ Retorna uma representação da amostra seguindo o schema definido em
        AmostraViewSchema.
    """
    result = []
    for amostra in amostras:
        result.append({

        "id": amostra.id,
        "numero": amostra.numero,
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
    


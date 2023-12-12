from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity, Potability (outcome)

class Amostra(Base):
    __tablename__ = 'amostras'
    
    id = Column(Integer, primary_key=True)
    numero= Column("numero", Integer)
    ph = Column("Ph", Float)
    hardness = Column("Hardness", Float)
    solids = Column("Solids", Float)
    chloramines = Column("Chloramines", Float)
    sulfate = Column("Sulfate,", Float)
    conductivity = Column("Conductivity", Float)
    organic_carbon = Column("Organic_carbon", Float)
    trihalomethanes = Column("Trihalomethanes", Float)
    turbidity = Column("Turbidity", Float)
    outcome = Column("Diagnostic", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, numero:int, ph:float , hardness:float, solids:float, chloramines:float,
                 sulfate:float, conductivity:float, organic_carbon:float, 
                 trihalomethanes:float, turbidity:float, outcome:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma amostra

        """   
        self.numero= numero
        self.ph = ph
        self.hardness = hardness
        self.solids = solids
        self.chloramines = chloramines
        self.sulfate = sulfate
        self.conductivity = conductivity
        self.organic_carbon = organic_carbon
        self.trihalomethanes = trihalomethanes
        self.turbidity = turbidity
        self.outcome = outcome
    

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
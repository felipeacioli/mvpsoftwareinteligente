from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity, Potability (outcome)

class Amostra(Base):
    __tablename__ = 'amostras'
    
    id = Column(Integer, primary_key=True)
    ph = Column("Ph", Float)
    hardness = Column("Hardness", Float)
    solids = Column("Solids", Float)
    chloramines = Column("Chloramines", Float)
    sulfate = Column("Sulfate,", Float)
    conductivity = Column("Conductivity", Float)
    organic_carbon = Column("Organic_carbon", Float)
    trihalomethanes = Column("Trihalomethanes", Float)
    turbidity = Column("Turbidity", Float)
    outcome = Column("Potability", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, ph:float , hardness:float, solids:float, chloramines:float,
                 sulfate:float, conductivity:float, organic_carbon:float, 
                 trihalomethanes:float, turbidity:float, outcome:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria uma amostra

        Arguments:

            ph: o pH mede a acidez ou alcalinidade da água numa escala de 0 a 14, com 7 sendo neutro. Valores abaixo de 7 indicam acidez e acima de 7, alcalinidade. A água potável deve ter pH entre 6,5 e 8,5.
            hardness: dureza - Refere-se à concentração de íons de cálcio e magnésio na água. Água dura pode causar acúmulo de incrustações em canos e reduzir a eficácia de sabões.
            solids: sólidos (Sólidos Totais Dissolvidos, STD) - Refere-se à concentração de substâncias dissolvidas na água, como sais, minerais e metais.
            chloramines: cloraminas - Um desinfetante usado no tratamento de água que é uma combinação de cloro e amônia. É menos agressivo do que o cloro e proporciona uma desinfecção de longa duração.
            sulfate: sulfato - Uma substância que ocorre naturalmente na água, muitas vezes derivada de rochas ou poluição industrial. Níveis altos podem ter um efeito laxante.
            conductivity: condutividade - Mede a capacidade da água de conduzir eletricidade, o que está diretamente relacionado à concentração de sais ou íons dissolvidos na água.
            organic_carbon: carbono Orgânico (Carbono Orgânico Total, COT) - Refere-se à quantidade de carbono em compostos orgânicos presentes na água, um indicador de contaminação potencial por materiais orgânicos.
            trihalomethanes: trihalometanos (THMs) - Compostos químicos formados quando o cloro reage com matéria orgânica na água. Eles são considerados um risco à saúde em níveis elevados, associados a potenciais riscos de câncer.
            turbidity: turbidez - Refere-se à nebulosidade ou opacidade da água causada pela presença de partículas em suspensão. Alta turbidez pode indicar contaminação e afetar a qualidade da água.         
            outcome: potabilidade
            data_insercao: data de quando a amostra foi inserida à base
        """

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
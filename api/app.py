from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import *
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
amostra_tag = Tag(name="Amostra", description="Adição, visualização, remoção e predição da potabilidade em amostras de água")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de amostras

@app.get('/amostras', tags=[amostra_tag],
         responses={"200": AmostraViewSchema, "404": ErrorSchema})
def get_amostras():
    """Lista todas as amostras de água cadastrados na base
    Retorna uma lista de amostras cadastrados na base.
    
    """
    logger.debug("Coletando dados de todas as amostras")
    session = Session()
    
    # Buscando todas as amostras
    amostras = session.query(Amostra).all()
    
    if not amostras:
        logger.warning("Não há amostras cadastrados na base :/")
        return {"message": "Não há amostras cadastrados na base :/"}, 404
    else:
        logger.debug(f"%d amostras econtradas" % len(amostras))
        return apresenta_amostras(amostras), 200


# Rota de adição de amostra
@app.post('/amostra', tags=[amostra_tag],
          responses={"200": AmostraViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: AmostraSchema):
    """Adiciona uma nova amostra à base de dados
    Retorna uma representação das amostras e diagnósticos associados.

    """
    # TODO: Instanciar classes

    # Recuperando os dados do formulário
    
    ph = form.ph
    hardness = form.hardness
    solids = form.solids
    chloramines = form.chloramines
    sulfate = form.sulfate
    conductivity = form.conductivity
    organic_carbon = form.organic_carbon 
    trihalomethanes = form.trihalomethanes
    turbidity = form.turbidity

    # Preparando os dados para o modelo
    X_input = PreProcessador.preparar_form(form)
    # Carregando modelo
    model_path = 'MachineLearning/pipelines/rf_water_pipeline.pkl'
    # modelo = Model.carrega_modelo(ml_path)
    modelo = Pipeline.carrega_pipeline(model_path)
    # Realizando a predição
    outcome = int(Model.preditor(modelo, X_input)[0])

    # Carregando modelo
    #ml_path = 'ml_model/modelo_treinado.pkl'
    #modelo = Model.carrega_modelo(ml_path)##
    
    amostra = Amostra(
        
        ph=ph,
        hardness=hardness,
        solids=solids,
        chloramines=chloramines,
        sulfate=sulfate,
        conductivity=conductivity,
        organic_carbon=organic_carbon,
        trihalomethanes=trihalomethanes,
        turbidity=turbidity,
        outcome=outcome

    )
    
    logger.debug(f"Adicionando amostra")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se amostra já existe na base
       # if session.query().filter(Amostra.numero == form.numero).first():
            #error_msg = "Amostra já existente na base :/"
            #logger.warning(f"Erro ao adicionar amostra '{amostra.numero}', {error_msg}")
            #return {"message": error_msg}, 409
        
        # Adicionando amostra
        session.add(amostra)
        
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado amostra!")
        return apresenta_amostra(amostra), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar amostra")
        return {"message": error_msg}, 400
       
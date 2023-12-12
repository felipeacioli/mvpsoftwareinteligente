from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Amostra, Model
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
amostra_tag = Tag(name="Amostra", description="Adição, visualização, remoção e predição da potabilidade amostras de água")


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
    
    # Carregando modelo
    ml_path = 'ml_model/modelo_treinado.pkl'
    modelo = Model.carrega_modelo(ml_path)
    
    amostra = Amostra(

        numero=form.numero,
        ph=form.ph,
        hardness=form.hardness,
        solids=form.solids,
        chloramines=form.chloramines,
        sulfate=form.sulfate,
        conductivity=form.conductivity,
        organic_carbon=form.organic_carbon,
        trihalomethanes=form.trihalomethanes,
        turbidity=form.turbidity,
        outcome=Model.preditor (modelo, form)

    )
    
    logger.debug(f"Adicionando amostra de número: '{amostra.numero}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se amostra já existe na base
        if session.query().filter(Amostra.numero == form.numero).first():
            error_msg = "Amostra já existente na base :/"
            logger.warning(f"Erro ao adicionar amostra '{amostra.numero}', {error_msg}")
            return {"message": error_msg}, 409
        
        # Adicionando amostra
        session.add(amostra)
        
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado amostra de número: '{amostra.numero}'")
        return apresenta_amostra(amostra), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar amostra '{amostra.numero}', {error_msg}")
        return {"message": error_msg}, 400
    

# Métodos baseados em nome
# Rota de busca de paciente por nome
@app.get('/amostra', tags=[amostra_tag],
         responses={"200": AmostraViewSchema, "404": ErrorSchema})
def get_amostra(query: AmostraBuscaSchema):    
    """Faz a busca por uma amostra cadastrada na base a partir do número

    """
    
    amostra_numero = query.numero
    logger.debug(f"Coletando dados sobre amostra #{amostra_numero}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    amostra = session.query(Amostra).filter(Amostra.numero == amostra_numero).first()
    
    if not amostra:
        # se a amostra não foi encontrada

        error_msg = f"Amostra {amostra_numero} não encontrada na base :/"
        logger.warning(f"Erro ao buscar amsotra '{amostra_numero}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Amostra econtrada: '{amostra.numero}'")
        # retorna a representação do paciente
        return apresenta_amostra(amostra), 200
   
    
# Rota de remoção de amostra por número
@app.delete('/amostra', tags=[amostra_tag],
            responses={"200": AmostraViewSchema, "404": ErrorSchema})
def delete_amostra(query: AmostraBuscaSchema):
    """Remove uma amostra cadastrada na base a partir do número

    """
    
    amostra_numero = unquote(query.numero)
    logger.debug(f"Deletando dados sobre amostra #{amostra_numero}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando amostra
    amostra = session.query(Amostra).filter(Amostra.numero == amostra_numero).first()
    
    if not amostra:
        error_msg = "Amostra não encontrado na base :/"
        logger.warning(f"Erro ao deletar amostra'{amostra_numero}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(amostra)
        session.commit()
        logger.debug(f"Deletado amostra #{amostra_numero}")
        return {"message": f"Amostra {amostra_numero} removida com sucesso!"}, 200


        
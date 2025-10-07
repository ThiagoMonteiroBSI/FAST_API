from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Produto(BaseModel):
      id: int
      nome : str 
      preco : float

produtos = [
    {"id": 1, "nome": "Notebook","preco":2500},
    {"id": 2, "nome": "Monitor","preco":3000},
    {"id": 3, "nome": "Mouse","preco":200},
    {"id": 4, "nome": "Teclado","preco":320},
    {"id": 7, "nome": "Makita","preco":788},
]

ultimo_id_produto = 5


@app.get("/")
def hello():
    return {'mensagem': 'Olá Mundao '}

@app.get("/produtos", response_model=list[Produto])
def listar_produtos():
    return produtos 

@app.get("/produtos/{id}", response_model=Produto)
def obter_produto(id: int):
    for produto in produtos:
        if produto["id"] == id:
            return produto
    return {"erro": "Produto nao encontrado"}            
        
@app.post("/produtos/")
def criar_produto(nome: str, preco:float):
     global ultimo_id_produto
     novo_produto = {'id': ultimo_id_produto +1, 'nome':nome, 'preco':preco}
     produtos.append(novo_produto)
     ultimo_id_produto +=1 
     return novo_produto
        



        
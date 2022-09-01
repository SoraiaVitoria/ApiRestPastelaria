from fastapi import APIRouter
from pydantic import BaseModel 

router = APIRouter()

class Produto(BaseModel):
    nome: str
    descricao: str
    foto: str
    valor_unitario: float

# Criar os endpoints de Produto: GET, POST, PUT, DELETE
@router.get("/produto/{id}", tags=["produto"])
def get_produto(id: int):
    return {"msg": "get executado"}, 200

@router.post("/produto/{id}", tags=["produto"])
def post_produto(id: int, p: Produto):
    return {"msg": "post executado", "id": id, "nome": p.nome, "descricao": p.descricao, "foto": p.foto, "valor_unitario": p.valor_unitario}, 200

@router.put("/produto/{id}", tags=["produto"])
def put_produto(id: int, p: Produto):
    return {"msg": "put executado", "id": id, "nome": p.nome, "descricao": p.descricao, "foto": p.foto, "valor_unitario": p.valor_unitario}, 200

@router.delete("/produto/{id}", tags=["produto"])
def delete_produto(id: int):
    return {"msg": "delete executado"}, 201
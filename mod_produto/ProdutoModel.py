from decimal import Decimal
import db
from sqlalchemy import Column, VARCHAR, Integer, BLOB, NUMERIC

# ORM
class ProdutoDB(db.Base): 
    __tablename__ = 'tb_produto'
    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(VARCHAR(100), nullable=False)
    foto = Column(BLOB, nullable=False)
    valor_unitario = Column(NUMERIC(11, 2), nullable=False)

    def __init__(self, id_produto, nome, descricao, foto, valor_unitario):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.foto = foto
        self.valor_unitario = valor_unitario
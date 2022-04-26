# from dataclasses import dataclass
# o dataclass gera objetos que são classes de dados
# dataclass embutida no Py

# models.py receberá a modelagem dos dados

#@dataclass 
#decorador que injeta novos métodos em class Beer

from sqlmodel import Optional
from sqlmodel import SQLModel, Field
from sqlmodel import select 
from pydantic import validator 

#add selct ao objeto 

class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str #dados vindos do mundo externo; garantir validação dos dados
    style: str
    flavor: int
    image: int
    cost: int
    # aplicações mais complexas: diagramas 

    @validator("flavor", "image", "cost")
    def validate_ratings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return v


brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=8, cost=8)
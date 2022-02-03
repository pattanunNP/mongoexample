from typing import Optional
from pydantic import BaseModel
from typing import Optional, List


class Pokemon(BaseModel):
          name: str
          description: Optional[str] = None
          type: str
          hp: int

class Pokemons(BaseModel):
          pokemons: List[Pokemon]



# pokemon[0].name
# pokemon[0].description
# pokemon[0].type

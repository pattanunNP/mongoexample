from fastapi import FastAPI, HTTPException
from schema import Pokemons
from mongo import MongoDBConnector
import pandas as pd

app = FastAPI()


database = MongoDBConnector.connect()

@app.get("/")
async def main():
          return {"message": "Hello World"}


@app.get("/pokemon")
async def get_pokemon(name: str):
          try:
                    collection = database.doc
                    pokemon = collection.find_one({"name": name})
                    result = {
                              
                              "name": pokemon["name"],
                              "type": pokemon["type"],
                              "hp": pokemon["hp"],
                              "description": pokemon["description"]
                                        
                    }
                    return result
                              
          except:
                    raise HTTPException(status_code=404, detail="Pokemon not found")

@app.post("/pokemon", status_code=201)
async def create_pokemon(req: Pokemons):

          collection = database.doc

          collection.insert_many(req.pokemons)


          return {"message": "Pokemon created"}

@app.post("pokemon/csv", status_code=201)
async def create_pokemon_csv(req: Pokemons):
          
                    data = pd.read_csv("pokemon.csv")

                    name = data["name"].str.lower()
                    type = data["type"].str.lower()
                    des  =    data["description"].str.lower()

                    return {"message": "Pokemon created"}



# 200 OK
# 201 Created
# 202 Accepted

# 300 Multiple Choices
# 301 Moved Permanently
# 302 Found
# 303 See Other

# 400 Bad Request
# 401 Unauthorized
# 403 Forbidden
# 404 Not Found
# 405 Method Not Allowed
# 406 Not Acceptable

# 500 Internal Server Error
# 501 Not Implemented
# 502 Bad Gateway
# 503 Service 

# google.com 
# app.facebook.com
# ads.google.com
#
# m.facebook.com

# jamwnk.com 

# ig.meta.com

# scb.co.th
# scb.net


# uuid :1223

# database => collection => document => field => value
# database => table => row => column => value

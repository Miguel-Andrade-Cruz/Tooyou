from pydantic import BaseModel



class DisposablesType(BaseModel):

    items: list[dict]
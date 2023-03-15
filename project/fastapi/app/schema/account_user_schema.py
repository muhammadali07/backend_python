from pydantic import BaseModel
from typing import Optional


class AccountUser(BaseModel):
    username : Optional[str] = 'Muh Ali Bakhtiar'
    email: Optional[str] = 'muhalibakhtiar@gmail.com'
    password: Optional[str]= 'ali12344'
    role: Optional[str] = 'admin'
    divisi: Optional[str] = 'engineering'

class AccountLogin(BaseModel):
    email: Optional[str] = 'muhalibakhtiar@gmail.com'
    password: Optional[str]= 'ali12344'
import jwt

from fastapi import Depends, HTTPException # type: ignore
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials # type: ignore
from jwt import PyJWTError, decode
from datetime import datetime, timedelta
from typing import Optional
from jwt import PyJWTError, decode

SECRET_KEY = "secret_key"  # ganti dengan secret key yang sesuai
ALGORITHM = "HS256"

bearer_scheme = HTTPBearer()

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)  # waktu kedaluwarsa default
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Fungsi untuk memverifikasi token
async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    try:
        # Ambil token dari credentials
        token = credentials.credentials
        # Decode token dengan menggunakan secret key dan algorithm yang sama pada saat generate token
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Ambil waktu saat ini
        now = datetime.utcnow()
        # Ambil waktu kedaluwarsa token dari payload
        expire = datetime.fromtimestamp(payload["exp"])
        # Jika waktu sekarang lebih besar dari waktu kedaluwarsa token, raise HTTPException dengan status code 401
        if now > expire:
            raise HTTPException(status_code=401, detail="Token has expired")
    except PyJWTError:
        # Jika token invalid atau error decode, raise HTTPException dengan status code 401
        raise HTTPException(status_code=401, detail="Invalid token")
    # Jika token valid dan belum kadaluwarsa, return payload
    return payload

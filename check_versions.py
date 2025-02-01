import pyarrow
import pandas as pd
import boto3
import dotenv

print("pyarrow version:", pyarrow.__version__)
print("pandas version:", pd.__version__)
print("boto3 version:", boto3.__version__)

# Verificar se dotenv está instalado
print("dotenv is installed:", dotenv is not None)

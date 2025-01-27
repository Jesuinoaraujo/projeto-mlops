import os
from minio import Minio
from minio.error import S3Error

# Configurações do MinIO
MINIO_ENDPOINT = "192.168.15.200:9000"
MINIO_ACCESS_KEY = "minioadmin"
MINIO_SECRET_KEY = "minioadmin"

# Cria um cliente MinIO
client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

# Função para copiar arquivos de um bucket para outro


def copy_files(source_bucket, destination_bucket, filenames):
    for file_name in filenames:
        try:
            # Baixa o arquivo do bucket de origem
            client.fget_object(source_bucket, file_name, file_name)
            # Envia o arquivo para o bucket de destino
            client.fput_object(destination_bucket, file_name, file_name)
            print(f"Arquivo '{file_name}' copiado de '{
                  source_bucket}' para '{destination_bucket}'.")
        except S3Error as err:
            print(f"Erro ao copiar o arquivo '{file_name}': {err}")


# Arquivos a serem copiados
filenames = ['nafld1.csv', 'nafld2.csv']

# Copia os arquivos do bucket 'raw' para o bucket 'bronze'
copy_files('raw', 'bronze', filenames)

# Remove os arquivos temporários locais depois de copiar
for file_name in filenames:
    if os.path.exists(file_name):
        os.remove(file_name)

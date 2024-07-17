import redis
import os

# Defina o host e a porta do Redis com base nos valores do serviço
redis_host = "35.239.233.36"  # Substitua pelo IP externo do seu serviço Redis
redis_port = 6379             # Porta onde o Redis está escutando

try:
    # Conecte-se ao Redis
    redis_client = redis.Redis(host=redis_host, port=redis_port)

    # Teste a conexão com o comando PING
    response = redis_client.ping()

    if response:
        print("Conexão com o Redis bem-sucedida!")
    else:
        print("Conexão com o Redis falhou!")

except Exception as e:
    print(f"Erro ao conectar ao Redis: {e}")
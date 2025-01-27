import subprocess
import os

# Caminho para o arquivo de log
log_file = "installation_logs.txt"

# Comandos a serem executados e registrados
commands = [
    "pip install --timeout=1000 -r requirements_base.txt",
    "pip install --timeout=1000 -r requirements_airflow.txt"
]

# Função para executar comandos e capturar logs


def execute_and_log(commands, log_file):
    with open(log_file, "w") as logfile:
        for command in commands:
            process = subprocess.Popen(
                command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            logfile.write(f"Command: {command}\n")
            logfile.write("Output:\n")
            logfile.write(stdout)
            logfile.write("Errors:\n")
            logfile.write(stderr)
            logfile.write("\n" + "="*40 + "\n")


# Executar e registrar comandos
execute_and_log(commands, log_file)

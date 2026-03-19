import paramiko
import time

client = paramiko.SSHClient()

# 1. Aceptar host automáticamente
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 2. Conectarse
client.connect("10.192.3.25", username="40884366", password="123456")

# 3. Abrir terminal interactiva
shell = client.invoke_shell()

time.sleep(1)

# 4. Enviar comando
shell.send("whoami\n")

time.sleep(1)

# 5. Leer respuesta
if shell.recv_ready():
    output = shell.recv(5000).decode()
    print(output)

# 6. Cerrar conexión
client.close()
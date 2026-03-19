import telnetlib
import time
import os

# Functions
def ping(host):
    response = os.system(f"ping -n 1 {host}")  # Windows
    # response = os.system(f"ping -c 1 {host}")  # Linux/Mac
    return response == 0

HOST = "10.192.3.25"
PORT = 23
USER = "40884366"
PASSWORD = "123456"

def main():

  if ping("10.192.3.25"):
      print("✅ Controlador activo")
      tn = telnetlib.Telnet(HOST, PORT)

      time.sleep(1)
      # print(tn.read_very_eager().decode('latin-1'))

      # Enviar usuario
      tn.read_until("Operador".encode('latin-1'))
      tn.write(b"40884366\r\n")
      time.sleep(2)
      # print(tn.read_very_eager().decode('latin-1'))
      
      # Enviar password
      tn.write(b"123456\r\n")
      time.sleep(5)
      # print(tn.read_very_eager().decode('latin-1'))

      # Enter letters menu
      time.sleep(5)
      # tn.read_until("PRINCIPAL".encode('latin-1'))
      tn.write(b"\x10")
      tn.write(b"\x10")
      # print(tn.read_very_eager().decode('latin-1'))

      # Enter letter c
      time.sleep(5)
      # tn.read_until("TECLAS".encode('latin-1'))
      tn.write(b"c\r\n")
      # print(tn.read_very_eager().decode('latin-1'))

      # Enter 1 (Funciones de terminal)
      time.sleep(5)
      # tn.read_until("Terminal".encode('latin-1'))
      tn.write(b"1\r\n")
      # print(tn.read_very_eager().decode('latin-1'))

      # Enter 7 (Cargar Memoria del Terminal)
      time.sleep(5)
      tn.write(b"7\r\n")
      # print(tn.read_very_eager().decode('latin-1'))

      # Enter ID caja
      time.sleep(5)
      tn.write(b"103\r\n")
      time.sleep(2)
      # print(tn.read_very_eager().decode('latin-1'))

      tn.close()

  else:
      print("❌ No responde")

if __name__ == "__main__":
    main()
import csv
import pywhatkit
import time
import os
os.environ["DISPLAY"] = ":0"
os.environ["XAUTHORITY"] = "/home/m87/.Xauthority"

# Configuración importante
espera_entre_mensajes = 10  # Segundos entre mensajes para evitar bloqueos
tiempo_espera_whatsapp = 15  # Tiempo para cargar WhatsApp Web

# Leer la plantilla del mensaje
with open('message.txt', 'r', encoding='utf-8') as file:
    plantilla_mensaje = file.read()

# Leer el archivo CSV con los contactos
with open('data.csv', 'r', encoding='utf-8') as file:
    lector_csv = csv.DictReader(file)
    
    for fila in lector_csv:
        try:
            # Limpieza y formato del número telefónico
            numero = fila['numero'].strip()
            numero = numero.replace('+', '').replace(' ', '').replace('-', '')
            
            # Formatear el mensaje personalizado
            mensaje_personalizado = plantilla_mensaje.format(**fila)
            
            # Enviar el mensaje via WhatsApp
            pywhatkit.sendwhatmsg_instantly(
                phone_no=numero,
                message=mensaje_personalizado,
                wait_time=tiempo_espera_whatsapp
            )
            
            print(f"✅ Mensaje enviado a {fila['nombre']} - {numero}")
            
            # Espera entre mensajes
            time.sleep(espera_entre_mensajes)
            
        except Exception as e:
            print(f"❌ Error con {fila.get('nombre', 'contacto desconocido')}: {str(e)}")
            continue

print("Proceso completado. Revisa los resultados.")
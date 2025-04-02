# WhatsApp Auto Memory Doll

Un script para enviar mensajes a múltiples usuarios de WhatsApp utilizando una lista.

## Características

- Envío automatizado de mensajes a contactos de WhatsApp
- Personalización de mensajes usando variables
- Gestión de contactos mediante archivo CSV
- Fácil configuración y uso

## Requisitos

- Python 3.6 o superior
- Cuenta de WhatsApp con sesión activa en WhatsApp Web

## Instalación

### En Linux

```bash
# Clonar el repositorio
git clone https://github.com/yourusername/whatsapp-auto-memory-doll.git
cd whatsapp-auto-memory-doll

# Crear entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

1. Edita el archivo `data.csv` con la información de tus contactos:
  ```
  nombre,numero
  Juan,1234567890
  Maria,9876543210
  ```
  (Solo incluir números sin espacios, símbolos ni código de país)

2. Personaliza el mensaje en `message.txt` utilizando f-strings:
  ```
  Hola {nombre}, este es un mensaje automatizado.
  ```

3. Ejecuta el script:
  ```bash
  python script.py
  ```

## Licencia

[LICENSE](LICENSE)
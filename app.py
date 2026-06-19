import requests

def consultar_dni(dni_numero, token):
    # Endpoint oficial de apiperu.dev para consultas DNI
    url = "https://apiperu.dev/api/dni"
    
    # Configuramos los datos que viajan en el cuerpo de la petición (JSON)
    payload = {
        "dni": str(dni_numero)
    }
    
    # Configuramos las cabeceras obligatorias y la autenticación
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    try:
        # Realizamos la petición POST enviando los datos en formato JSON
        respuesta = requests.post(url, json=payload, headers=headers)
        
        # Si el servidor responde exitosamente (Código 200)
        if respuesta.status_code == 200:
            resultado = respuesta.json()
            
            if resultado.get("success"):
                return resultado.get("data")
            else:
                print("La API no pudo encontrar información para ese DNI.")
                return None
        else:
            print(f"Error en el servidor de la API. Código de estado: {respuesta.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Ocurrió un error de conexión: {e}")
        return None

# ==========================================
# EJEMPLO DE USO DEL CÓDIGO
# ==========================================

# 1. Coloca aquí el Token que te da tu proveedor de APIs
MI_TOKEN = "toquen del usuario"

# 2. El número de DNI que quieres buscar
dni_a_buscar = "7777777"  # Reemplaza por un DNI real para probar

print(f"Consultando el DNI: {dni_a_buscar}...")
datos_persona = consultar_dni(dni_a_buscar, MI_TOKEN)

if datos_persona:
    print("\n--- ¡Datos Encontrados! ---")
    print(f"Nombre Completo: {datos_persona.get('nombre_completo')}")
    print(f"Nombres: {datos_persona.get('nombres')}")
    print(f"Apellido Paterno: {datos_persona.get('apellido_paterno')}")
    print(f"Apellido Materno: {datos_persona.get('apellido_materno')}")
    print(f"Código de Verificación (Dígito después del guión): {datos_persona.get('codigo_verificacion')}")
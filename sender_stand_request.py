import configuration
import requests
import data



# Función para obtener la documentación
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

# Solicitud y respuesta de ejemplo para documentación
response = get_docs()
print(response.status_code)


# Función para crear un nuevo usuario
def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )

# Solicitud y respuesta de ejemplo para crear un nuevo usuario
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

# Función para crear un nuevo kit de productos
def post_new_kit(body, token):
    headers = {"Authorization": f"Bearer {token}"}
    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=body,
        headers=headers
    )

# Ejemplo de solicitud y respuesta para crear un nuevo kit
example_kit_body = {
    "name": "Test Kit"
}
auth_token = "your_auth_token"  # Debes obtener un token válido
response = post_new_kit(example_kit_body, auth_token)
print(response.status_code)
print(response.json())
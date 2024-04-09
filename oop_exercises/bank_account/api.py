import requests
# import fastapi

# app = fastapi.FastAPI()


base_url = 'https://petstore.swagger.io/v2/'

def get_available_pets():
    url = base_url + "pet/findByStatus?status=available"
    response = requests.get(url)
    return response.json()


def add_new_pet(pet_data):
    url = base_url + "pet"
    response = requests.post(url, json=pet_data)
    return response.json()

def update_new_pet(pet_id, pet_updated_data):
    url = base_url + "pet"
    response = requests.post(url, json = pet_updated_data)
    return response.status_code, response.json()
    
if __name__ == '__main__':
    available_pets = get_available_pets()
    print("Available pets:", available_pets)
    
    new_pet_data = {
        "id": 12345,
        "name": "Fluffy",
        "status": "available"
    }
    
    pet_id = 12345
    updated_data = {
        "id": pet_id,
        "name": "bublick",
        "status": "dead"
    }

    added_pet = add_new_pet(new_pet_data)
    print("Added pet:", added_pet)

    status_code, response_json = update_new_pet(pet_id, updated_data)
    print(response_json)
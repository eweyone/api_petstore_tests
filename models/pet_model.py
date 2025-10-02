


class PetAPI:
    def __init__(self, client):
        self.client = client

    def create_pet(self, pet_data):
        return self.client.post('/pet', json=pet_data)

    def get_pet(self, pet_id):
        return self.client.get(f'/pet/{pet_id}')

    def update_pet(self, pet_data):
        return self.client.put('/pet', json=pet_data)

    def delete_pet(self, pet_id):
        return self.client.delete(f'/pet/{pet_id}')
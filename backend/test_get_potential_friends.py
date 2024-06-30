# test_get_potential_friends.py
from app import create_app
from flask_jwt_extended import create_access_token

app = create_app()

with app.app_context():
    from model.user import User
    token = create_access_token(identity='existing_user_id')  # Replace with an actual user ID
    headers = {
        'Authorization': f'Bearer {token}'
    }
    client = app.test_client()
    response = client.get('/api/potential_friends', headers=headers)
    print(response.get_json())

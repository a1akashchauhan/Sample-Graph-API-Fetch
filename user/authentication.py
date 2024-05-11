import json

def authenticate(UID):
    mock_token_data= {
        "social_media_tokens": [
            {
                "UID": "U0001",
                "platform_name": "Instagram",
                "access_token": "ig_token_123456",
                "expiry_date": "2024-12-31",
                "refresh_token": "ig_refresh_token_abcdef"
            },
            {
                "UID": "U0002",
                "platform_name": "Instagram",
                "access_token": "ig_token_789012",
                "expiry_date": "2024-12-31",
                "refresh_token": "ig_refresh_token_xyz123"
            },
            {
                "UID": "U0003",
                "platform_name": "Instagram",
                "access_token": "instagram_token_345678",
                "expiry_date": "2024-12-31",
                "refresh_token": "ig_refresh_token_123xyz"
            }
        ]
    }



    data= mock_token_data


  
    token_data = next((token for token in data['social_media_tokens'] if token['UID'] == UID), None)
    
    return token_data

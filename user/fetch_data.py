import json

analytics_data={
  "social_media_tokens": [
    {
      "platform_name": "Instagram",
      "access_token": "ig_token_123456",
      "total_views": 10000,
      "growth_rate": 0.05,
      "total_followers": 50000,
      "total_likes": 2000,
      "total_comments": 500
    },
    {
      "platform_name": "Instagram",
      "access_token": "ig_token_789012",
      "total_views": 5000,
      "growth_rate": 0.03,
      "total_followers": 30000,
      "total_likes": 1500,
      "total_comments": 300
    },
    {
      "platform_name": "Instagram",
      "access_token": "instagram_token_345678",
      "total_views": 20000,
      "growth_rate": 0.08,
      "total_followers": 80000,
      "total_likes": 3000,
      "total_comments": 700
    }
  ]
}

def fetch_analytics_data(access_token):
    data = analytics_data
    token_data = next((token for token in data['social_media_tokens'] if token['access_token'] == access_token), None)

    return token_data

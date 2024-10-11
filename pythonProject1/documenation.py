import requests

if __name__ == '__main__':
    api_key = 'xKqD0tQzma-IpX1OF5t_iA'  # Asegúrate de que no haya espacios extra
    headers = {'Authorization': 'Bearer ' + api_key}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    params = {
        'linkedin_profile_url': 'https://linkedin.com/in/johnrmarty/',
    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=headers)

    print(f'Status Code: {response.status_code}')
    print(f'Response Text: {response.text}')
    print(headers)

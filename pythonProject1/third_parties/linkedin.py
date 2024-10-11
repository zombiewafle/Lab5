import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    """Scrape information from LinkedIn profiles manually or using an API."""

    if mock:
        linkedin_profile_url='https://gist.githubusercontent.com/rogerdiaz/2d10d662484e892c83106b749b6b8d27/raw/316ff86d46bf2da7b0fa00b8ac149ebe38d894b3/roger-diaz.json'
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )

    else:
        api_key = os.environ.get("PROXYCURL_API_KEY")
        headers = {'Authorization': 'Bearer ' + api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        linkedin_profile_url = 'https://www.linkedin.com/in/roger-d%C3%ADaz-0946758b/'

        response = requests.get(api_endpoint,
                                params={'url': linkedin_profile_url},
                                headers=headers)

    data = response.json()

    return data



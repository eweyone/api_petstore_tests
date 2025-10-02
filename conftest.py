import pytest
from utils.api_client import APIClient
import logging



def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('petstore_test.log'),
            logging.StreamHandler()
        ]
    )

setup_logging()
logger = logging.getLogger('petsore_tests')

@pytest.fixture
def petstore_client():
    return APIClient('https://petstore.swagger.io/v2')
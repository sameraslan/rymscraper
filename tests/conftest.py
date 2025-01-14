from rymscraper import RymNetwork
import pytest


# @pytest.fixture
@pytest.fixture(scope="session", autouse=True)
def network():
    network = RymNetwork(headless=True)
    yield network
    network.browser.close()
    network.browser.quit()

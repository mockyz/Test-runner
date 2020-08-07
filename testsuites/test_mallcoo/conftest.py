import pytest
from api.demo import mallcoo as MallcooAPI
from .mallcoo_base_config import MData


@pytest.fixture()
def login():
    inputs = MData.Login_Data_Case()
    api = MallcooAPI.Login().with_body_params(MallID=inputs["mallid"], Mobile=inputs["mobile"], Pwd=inputs['pwd'])
    response = api.invoke()
    assert response.get_status_code() == 200
    assert response.get_response_attr('m') == 1
    assert response.get_response_attr('d')['MallID'] == 10296
    token = response.get_response_attr('d')['Token']
    return token

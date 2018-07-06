import allure
import pytest

class Test_allure:
    def setup(self):
        pass
    def teardown(self):
        pass

    @pytest.mark.parametrize("a",[1,2,3])
    @allure.step("我是测试步骤001")
    def test_01(self,a):
        assert a != 2

    def test_02(self):

        allure.attach("描述","我是测试步骤02的描述-----")
        assert 1








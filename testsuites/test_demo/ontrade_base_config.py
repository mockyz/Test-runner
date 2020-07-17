# -- coding: utf-8 --

from testsuites.test_demo.utils import *

Address_TEMPLATE = {"onTrade_noTrans": "AGzR6XXrXJq8htfwLQaeYJHHiZ7YvtgGYE",
                    "onTrade_trans": "AcCj3eVyaHjMuHJQEg7QoHoZv7txgrwKNw",
                    "outTrade_trans": "AHe5NrFRBWYaJo9uB5iQkViXQ7naqQ8y6a",
                    "outTrade_noTrans": "AZdoEohxjH8Jz3W8GjiCosUimRqQCkvUgX",
                    "error": "AcCj3eVyaHjMuHJQEg7QoHoZv7txgrwKNw88"}


class OntradeBaseConfig:

    CoinType = "ONT"
    Address = Address_TEMPLATE

    def set_config(self, coinType="", Address=Address_TEMPLATE):
        self.CoinType = coinType
        self.Address = Address

    def CREATE_ADDRESS_CASES(self):
        CREATE_ADDRESS_CASES = [("创建一个地址", [{"coinType": self.CoinType}], 0),
                                ("创建3个地址", [{"coinType": self.CoinType}, {"coinType": self.CoinType},
                                            {"coinType": self.CoinType}], 0)
            , ("地址coinType小写创建失败", [{"coinType": self.CoinType.lower()}], 1),
                                ("部分成功部分失败", [{"coinType": self.CoinType}, {"coinType": self.CoinType + "X"}], 2)]
        return CREATE_ADDRESS_CASES

    def CHECK_ADDRESS_CASES(self):
        CHECK_ADDRESS_CASES = [("交易所创建无交易地址", self.Address["onTrade_noTrans"], {"result": "0", "hasTx": "1"}),
                               ("交易所创建有交易地址", self.Address["onTrade_trans"], {"result": "0", "hasTx": "1"}),
                               ("非交易所创建有交易地址", self.Address["outTrade_trans"], {"result": "0", "hasTx": "0"}),
                               ("非交易所创建无交易地址", self.Address["outTrade_noTrans"], {"result": "0", "hasTx": "1"}),
                               ("错误的地址", self.Address["error"], {"result": "1", "hasTx": "1"})]
        return CHECK_ADDRESS_CASES

    def QUERY_BANLANCE_CASES(self):
        QUERY_BANLANCE_CASES = [
            ("交易所内部地址", [{"coinType": self.CoinType, "coldWalletAddr": self.Address["onTrade_noTrans"]}], 0),
            ("交易所外部地址", [{"coinType": self.CoinType, "coldWalletAddr": self.Address["onTrade_trans"]}], 0),
            ("同时查询三个地址", [{"coinType": self.CoinType, "coldWalletAddr": self.Address["onTrade_trans"]},
                          {"coinType": self.CoinType, "coldWalletAddr": self.Address["onTrade_noTrans"]},
                          {"coinType": self.CoinType, "coldWalletAddr": self.Address["onTrade_trans"]}], 0)
            , ("错误的地址", [{"coinType": self.CoinType, "coldWalletAddr": self.Address["error"]}], 1), (
                "同时查询2个地址1个无效", [{"coinType": self.CoinType, "coldWalletAddr": self.Address["onTrade_trans"]},
                                 {"coinType": self.CoinType, "coldWalletAddr": self.Address["error"]}], 2)]
        return QUERY_BANLANCE_CASES

    def Set_Collectthreshold(self):
        Set_Collectthreshold = [
            ("设置一个币种", [{"coinType": self.CoinType, "threshold": "0.01"}], {"code": 0, "resCode": [0]}),
            ("设置三个币种",
             [{"coinType": self.CoinType, "threshold": "0.01"}, {"coinType": self.CoinType, "threshold": "0.01"},
              {"coinType": "BTC", "threshold": "0.01"}], {"code": 0, "resCode": [0, 0, 0]}),
            ("coinType小写失败", [{"coinType": self.CoinType.lower(), "threshold": "0.01"}], {"code": 1, "resCode": [1]}),
            ("两个均失败(阈值为特殊字符)",
             [{"coinType": self.CoinType, "threshold": "a"}, {"coinType": self.CoinType, "threshold": "~"}],
             {"code": 1, "resCode": [1, 1]}),
            ("两个均失败(阈值特殊字符和币种小写)",
             [{"coinType": self.CoinType.lower(), "threshold": "a"}, {"coinType": self.CoinType, "threshold": "~"}],
             {"code": 1, "resCode": [1, 1]}),
            ("设置三个币种一个失败",
             [{"coinType": self.CoinType, "threshold": "0.01"}, {"coinType": self.CoinType, "threshold": "0.01"},
              {"coinType": "PCX", "threshold": "-0.01"}], {"code": 2, "resCode": [0, 0, 1]})]
        return Set_Collectthreshold

    def Apply_For_Withdrawal(self):
        Apply_For_Withdrawal = [("生成一笔出金批次", [
            {"businessNo": "ONT001", "coinType": self.CoinType, "fromAddr": self.Address["outTrade_trans"],
             "data": [{"destAddr": self.Address["outTrade_trans"], "sendAmount": "0.005"}]}], {"code": 0}),
                                ("生成一笔出金批次失败，金额为-0.001",
                                 [{"businessNo": self.CoinType + business_no(), "coinType": self.CoinType,
                                   "fromAddr": self.Address["outTrade_trans"],
                                   "data": [{"destAddr": self.Address["outTrade_trans"],
                                             "sendAmount": "-0.001"}]}], {"code": 1}),
                                ("一个流水号生成2笔出金批次，金额为0.001和0.002",
                                 [{"businessNo": self.CoinType + business_no(), "coinType": self.CoinType,
                                   "fromAddr": self.Address["outTrade_trans"],
                                   "data": [{
                                       "destAddr": self.Address["outTrade_trans"],
                                       "sendAmount": "0.001"}, {
                                       "destAddr": self.Address["outTrade_trans"],
                                       "sendAmount": "0.002"}]}], {"code": 0}),
                                ("1个流水号生成2笔出金，金额为0.001和999999(金额大于热钱包地址出金失败)",
                                 [{"businessNo": self.CoinType + business_no(), "coinType": self.CoinType,
                                   "fromAddr": self.Address["outTrade_trans"],
                                   "data": [{
                                       "destAddr": self.Address["outTrade_trans"],
                                       "sendAmount": "0.001"}, {
                                       "destAddr": self.Address["outTrade_trans"],
                                       "sendAmount": "99999999"}]}],
                                 {"code": 1}),
                                ("1个流水号生成1笔出金，金额为0（币种差异、失败或成功、默认失败）",
                                 [{"businessNo": self.CoinType + business_no(), "coinType": self.CoinType,
                                   "fromAddr": self.Address["outTrade_trans"],
                                   "data": [{
                                       "destAddr": self.Address["outTrade_trans"],
                                       "sendAmount": "0"}]}], {"code": 1}),
                                ("1个流水号生成1笔出金，金额为a（特殊字符失败）", [{"businessNo": "ONT005", "coinType": self.CoinType,
                                                               "fromAddr": self.Address["outTrade_trans"],
                                                               "data": [{
                                                                   "destAddr": self.Address["outTrade_trans"],
                                                                   "sendAmount": "s"}]}], {"code": 1}),
                                ("2个流水号生成4笔出金，金额为0.001~0.004",
                                 [{"businessNo": self.CoinType + business_no(), "coinType": self.CoinType,
                                   "fromAddr": self.Address["outTrade_trans"],
                                   "data": [{
                                       "destAddr": self.Address["outTrade_trans"],
                                       "sendAmount": "0.001"}, {
                                       "destAddr": self.Address["outTrade_trans"],
                                       "sendAmount": "0.002"}]},
                                  {"businessNo": self.CoinType + business_no(), "coinType": self.CoinType,
                                   "fromAddr": self.Address["outTrade_trans"],
                                   "data": [{
                                       "destAddr": self.Address["outTrade_trans"],
                                       "sendAmount": "0.003"}, {
                                       "destAddr": self.Address["outTrade_trans"],
                                       "sendAmount": "0.004"}]}], {"code": 0})]
        return Apply_For_Withdrawal

    def With_Drawal_Bacth(self):
        With_Drawal_Bacth = [('不存在的batchID', 'No00000000000000', {"code": 1})]
        return With_Drawal_Bacth


BaseConfig = OntradeBaseConfig()

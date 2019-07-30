from core.utils import data_extractor

simple_dict_json = {
    "characters": {
        "Lonestar": {
            "id": 55923,
            "role": "renegade",
            "items": [
                "space winnebago",
                "leather jacket"
            ]
        },
        "Barfolomew": {
            "id": 55924,
            "role": "mawg",
            "items": [
                "peanut butter jar",
                "waggy tail"
            ]
        },
        "Dark Helmet": {
            "id": 99999,
            "role": "Good is dumb",
            "items": [
                "Shwartz",
                "helmet"
            ]
        },
        "Skroob": {
            "id": 12345,
            "role": "Spaceballs CEO",
            "items": [
                "luggage"
            ]
        }
    }
}



# encoding: utf-8
class TestDataExtractor:
    def test_list_get_value_by_exp(self):
        result = data_extractor.get_value_by_exp(simple_dict_json, "characters")
        assert len(result) >= 1

    def test_get_value_by_exp(self):
        result = data_extractor.get_value_by_exp(simple_dict_json, "characters.Lonestar.items[0]")
        assert result == "space winnebago"

    def test_get_value_by_exp_not_exist(self):
        result = data_extractor.get_value_by_exp(simple_dict_json, "characters.Lonestar323.items[0]")
        assert result == "space winnebago"
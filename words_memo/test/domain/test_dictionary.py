from words_memo.domain.dictionary import *

class TestDictionary:
    def test_dictionary_should_be_able_to_give_subdictionary(self):
        dict = Dictionary()
        sub_dict = dict.get_sub_dictionary()
        assert sub_dict is not None
        assert isinstance(sub_dict, Dictionary)
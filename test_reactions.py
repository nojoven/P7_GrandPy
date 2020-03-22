"""This file is used to test the functions of main.py"""
import os
import reactions
import nltk
nltk.download("stopwords")
nltk.download("punkt")


class TestReactions:
    """Pytest will be used to verify the behaviour of the following functions"""
    input_text = "GrandPy connais-tu l' Arc de Triomphe ?"
    conf = os.environ
    rX = reactions.Reactions()

    def test_process_words(self):
        """Testing the raw input"""
        process_words = self.rX.process_words(self.input_text)
        assert isinstance(process_words, list)
        assert len(process_words) > 0
        for word in process_words:
            assert isinstance(word, str)

    def test_get_input_(self):
        """Testing the formating of the input tu be used in a URL.
            Words must be separated by '+'.
        """
        process_words = self.rX.process_words(self.input_text)
        research = self.rX.get_input(process_words)
        assert research == "+".join(process_words)

    def test_get_coords(self):
        """Tests if we get the tuple of  latitude and longitude"""
        process_words = self.rX.process_words(self.input_text)
        research = self.rX.get_input(process_words)
        print(research)
        print(self.conf)
        coords = self.rX.get_coords(research, self.conf)
        assert coords is not None
        assert len(coords) == 2

    def test_get_map(self):
        """Tests if we fetch the map image as a JSON string"""
        process_words = self.rX.process_words(self.input_text)
        research = self.rX.get_input(process_words)
        location = self.rX.get_coords(research, self.conf)
        map_img = self.rX.get_map(research, location, self.conf)
        assert map_img is not None
        assert isinstance(map_img, str)

    def test_get_wiki(self):
        """Test to check if we get the Wikimedia summary"""
        process_words = self.rX.process_words(self.input_text)
        research = self.rX.get_input(process_words)
        location = self.rX.get_coords(research, self.conf)
        wiki_desc = self.rX.get_wiki(location)
        assert isinstance(wiki_desc, str)
        assert len(wiki_desc) > 0

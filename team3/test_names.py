from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Allan", "Gomes") == "Gomes;Allan"
    assert make_full_name("Aurora", "Matos") == "Matos;Aurora"

def test_extract_family_name():
    assert extract_family_name("Matos; Allan") == "Matos"
    assert extract_family_name("Maranhäo; Letïcia") == "Maranhäo"

def test_extract_given_name():
    assert extract_given_name("Matos; Allan") == "Allan"
    assert extract_given_name("Gomes; Angelo") == "Angelo"
    assert extract_given_name("Soares; Clara") == "Clara"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
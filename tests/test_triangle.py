from testprojectone.lib import try_me

def test_type_of_output():
    import matplotlib
    assert type(try_me(10, 10)) == matplotlib.figure.Figure

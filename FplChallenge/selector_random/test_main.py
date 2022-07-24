import json
import pathlib
import main
import pytest


def test_perform_selection_fails_on_empty_data():
    available_players = []

    with pytest.raises(AssertionError):
        main.perform_selection(available_players)


def test_perform_selection_fails_on_insuficient_data(available_players):
    available_players = available_players[:4]

    with pytest.raises(AssertionError):
        main.perform_selection(available_players)


def test_perform_selection_produces_valid_bench(available_players):

    selection = main.perform_selection(available_players)

    assert "bench" in selection

    bench = selection["bench"]

    assert len(bench) == 4
    assert bench[0]["pos"] == 1
    assert bench[1]["pos"] == 2
    assert bench[2]["pos"] == 3
    assert bench[3]["pos"] == 4


def test_perform_selection_produces_valid_squad(available_players):

    selection = main.perform_selection(available_players)

    assert "squad" in selection

    squad = selection["squad"]

    assert len(squad["goalkeepers"]) == 2
    assert len(squad["defenders"]) == 5
    assert len(squad["midfielders"]) == 5
    assert len(squad["forwarders"]) == 3


def test_perform_selection_produces_captain(available_players):

    selection = main.perform_selection(available_players)

    assert "captain" in selection

    captain = selection["captain"]

    assert "id" in captain


def test_perform_selection_produces_vice_captain(available_players):

    selection = main.perform_selection(available_players)

    assert "vice_captain" in selection

    vice_captain = selection["vice_captain"]

    assert "id" in vice_captain


def test_perform_selection_produces_different_captain_and_vice_captain(
    available_players,
):

    selection = main.perform_selection(available_players)

    vice_captain = selection["vice_captain"]
    captain = selection["captain"]

    assert captain["id"] != vice_captain["id"]


@pytest.fixture
def available_players():
    json_str = pathlib.Path("test_data/valid_available_players.json").read_text()
    return json.loads(json_str)

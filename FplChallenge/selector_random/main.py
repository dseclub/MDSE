import json
import requests
import random as rnd
from typing import Any, Dict, List

_API_URL_FPL_BOOTSTRAP_STATIC = (
    "https://fantasy.premierleague.com/api/bootstrap-static/"
)


def main():
    available_players = _fetch_available_playes(_API_URL_FPL_BOOTSTRAP_STATIC)

    return perform_selection(available_players)


def perform_selection(available_players: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Select and squad by random"""

    # 1. extract position players
    # 2. select squad by random
    # 3. select bench by random
    # 4. select captain and vice captain by random
    # 5. prepare for display

    goalkeepers, defenders, midfielders, forwarders = _extract_position_players(
        available_players
    )
    squad = _select_squad_by_random(goalkeepers, defenders, midfielders, forwarders)
    squad_bench = _select_bench_by_random(squad)
    squad_captain_and_vice_captain = _select_captain_and_vice_captain_by_random(
        squad, squad_bench
    )
    selection = _prepare_data_for_display(
        squad, squad_bench, squad_captain_and_vice_captain
    )

    return selection


def _fetch_available_playes(api_url_fpl_boostrap_static: str):
    """Fetch all available players from FPL"""

    assert api_url_fpl_boostrap_static is not None, "API URL is not set"

    json_response = requests.get(api_url_fpl_boostrap_static).json()

    assert "elements" in json_response, "No elements (players) in response"

    assert len(json_response["elements"]) > 400, "Player list is not long enough"

    return json_response["elements"]


def _extract_position_players(player_list: list) -> list:
    """Creates lists of players for each position"""

    goalkeeper = []
    defender = []
    midfielder = []
    forwarder = []

    for player in player_list:
        if player["element_type"] == 1:
            goalkeeper.append(player)
        if player["element_type"] == 2:
            defender.append(player)
        if player["element_type"] == 3:
            midfielder.append(player)
        if player["element_type"] == 4:
            forwarder.append(player)

    # checks outputs
    assert len(goalkeeper) >= 2, "There must be minimum 2 goalkeepers available"
    assert len(defender) >= 5, "There must be minimum 5 defenders available"
    assert len(midfielder) >= 5, "There must be minimum 5 midfielders available"
    assert len(forwarder) >= 3, "There must be minimum 3 forwarders available"

    return goalkeeper, defender, midfielder, forwarder

# TODO: Implement budget constraint
# TODO: Implement max-3 players from one team constraint

def _select_squad_by_random(
    goalkeepers: list,
    defenders: list,
    midfielders: list,
    forwarders: list,
) -> Dict[str, List[Dict[str, Any]]]:

    # 1. check inputs
    # 2. shuffle players
    # 3. assign players to squad at valid positions
    # 4. build list of all squad players
    # 5. check outputs

    # check inputs
    assert len(goalkeepers) >= 2, "There must be minimum goalkeepers available"
    assert len(defenders) >= 5, "There must be minimum defenders available"
    assert len(midfielders) >= 5, "There must be minimum midfielders available"
    assert len(forwarders) >= 3, "There must be minimum forwarders available"

    # shuffle position players
    rnd.shuffle(goalkeepers)
    rnd.shuffle(defenders)
    rnd.shuffle(midfielders)
    rnd.shuffle(forwarders)

    # populate squad
    squad = {"goalkeepers": [], "defenders": [], "midfielders": [], "forwarders": []}

    # there must be exactly 2 goalkeepers
    squad["goalkeepers"].append(goalkeepers.pop())
    squad["goalkeepers"].append(goalkeepers.pop())

    # there must be exactly 5 defenders
    squad["defenders"].append(defenders.pop())
    squad["defenders"].append(defenders.pop())
    squad["defenders"].append(defenders.pop())
    squad["defenders"].append(defenders.pop())
    squad["defenders"].append(defenders.pop())

    # there must be exactly 5 midfielders
    squad["midfielders"].append(midfielders.pop())
    squad["midfielders"].append(midfielders.pop())
    squad["midfielders"].append(midfielders.pop())
    squad["midfielders"].append(midfielders.pop())
    squad["midfielders"].append(midfielders.pop())

    # there must be exactly 3 forwarders
    squad["forwarders"].append(forwarders.pop())
    squad["forwarders"].append(forwarders.pop())
    squad["forwarders"].append(forwarders.pop())

    squad["all"] = (
        squad["goalkeepers"]
        + squad["defenders"]
        + squad["midfielders"]
        + squad["forwarders"]
    )

    # check outputs
    assert len(squad["goalkeepers"]) == 2, "Goalkeepers are not 2"
    assert len(squad["defenders"]) == 5, "Goalkeepers are not 5"
    assert len(squad["midfielders"]) == 5, "Goalkeepers are not 5"
    assert len(squad["forwarders"]) == 3, "Goalkeepers are not 3"

    return squad


def _select_bench_by_random(squad: Dict[str, list]) -> List[Dict[str, Any]]:

    # TODO: implement restrictions
    # - exactly one goalkeeper
    # - max 2 of defenders
    # - max 2 of forwarders

    # TODO: make more random
    # order on the bench matters
    # first element should be goakerkeeper
    # the elements 1-3 should be more random,
    # e.g. it could be 2 defenders and a forwarder
    # at the moment we pick one from each position

    squad_bench = [
        rnd.choice(squad["goalkeepers"]),
        rnd.choice(squad["defenders"]),
        rnd.choice(squad["midfielders"]),
        rnd.choice(squad["forwarders"]),
    ]

    assert len(squad_bench) == 4, "Squad bench does not have 4 players"

    return squad_bench


def _select_captain_and_vice_captain_by_random(
    squad: Dict[str, list], bench: list
) -> List[Dict[str, Any]]:
    captainable_players = [player for player in squad["all"] if player not in bench]

    assert len(captainable_players) == 11, "There must be 11 captainable players"

    rnd.shuffle(captainable_players[:])
    captain_and_vice_captain = rnd.sample(captainable_players, 2)

    assert (
        len(captain_and_vice_captain) == 2
    ), "There must be 2 players for captain and vice captain"

    return captain_and_vice_captain


def _trim_player_data_for_display(player: Dict) -> Dict:
    """Selects only few player descriptors for display"""

    # check input
    assert "id" in player, "Player has no id"
    assert "web_name" in player, "Player has no web_name"
    assert "element_type" in player, "Player has no element_type"
    assert "team" in player, "Player has no team"
    assert "now_cost" in player, "Player has no now_cost"

    return {
        "id": player["id"],
        "web_name": player["web_name"],
        "pos": player["element_type"],
        "team": player["team"],
        "now_cost": player["now_cost"]
    }


def _prepare_data_for_display(
    squad: Dict[str, list], squad_bench: list, squad_captain_and_vice_captain: list
) -> Dict[str, Any]:

    # check inputs
    assert len(squad["goalkeepers"]) == 2, "Goalkeepers are not 2"
    assert len(squad["defenders"]) == 5, "Goalkeepers are not 5"
    assert len(squad["midfielders"]) == 5, "Goalkeepers are not 5"
    assert len(squad["forwarders"]) == 3, "Goalkeepers are not 3"
    assert len(squad_bench) == 4, "Squad bench does not have 4 players"

    # limiting display data, skip this step to see more player data
    squad_for_display = {}
    squad_for_display["goalkeepers"] = list(
        map(_trim_player_data_for_display, squad["goalkeepers"])
    )
    squad_for_display["defenders"] = list(
        map(_trim_player_data_for_display, squad["defenders"])
    )
    squad_for_display["midfielders"] = list(
        map(_trim_player_data_for_display, squad["midfielders"])
    )
    squad_for_display["forwarders"] = list(
        map(_trim_player_data_for_display, squad["forwarders"])
    )
    squad_bench_for_display = list(map(_trim_player_data_for_display, squad_bench))
    squad_captain_and_vice_captain_for_display = list(
        map(_trim_player_data_for_display, squad_captain_and_vice_captain)
    )

    # check outputs
    assert len(squad_for_display["goalkeepers"]) == 2, "Goalkeepers are not 2"
    assert len(squad_for_display["defenders"]) == 5, "Goalkeepers are not 5"
    assert len(squad_for_display["midfielders"]) == 5, "Goalkeepers are not 5"
    assert len(squad_for_display["forwarders"]) == 3, "Goalkeepers are not 3"
    assert len(squad_bench_for_display) == 4, "Squad bench does not have 4 players"
    assert (
        len(squad_captain_and_vice_captain_for_display) == 2
    ), "Squad captain and vice captain does not have 2 players"

    selection = {}
    selection["squad"] = squad_for_display
    selection["bench"] = squad_bench_for_display
    selection["captain"] = squad_captain_and_vice_captain_for_display[0]
    selection["vice_captain"] = squad_captain_and_vice_captain_for_display[1]

    return selection


if __name__ == "__main__":
    selection = main()
    print("Selection:")
    print(json.dumps(selection, indent=2))

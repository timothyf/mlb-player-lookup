# MLB Player Lookup

This project provides scripts to look up MLB player IDs by their full name or by their MLBAM ID from a combined CSV file containing player information. If found the following player ids will be displayed: MLBAM, Baseball Reference, Retrosheet, and FanGraphs.

## Prerequisites

- Python 3.x
- pandas library

You can install the required library using pip:

```sh
pip install pandas
```

## Usage
To look up a player by their full name, run the player_lookup.py script with the player's full name as an argument:

```sh
python scripts/player_lookup.py "Player Name"
```

To look up a player by their MLBAM ID, run the reverse_lookup.py script with the player's MLBAM ID as an argument:

```sh
python scripts/reverse_lookup.py <mlbam_id>
```

### Example
```sh
python scripts/player_lookup.py "Riley Greene"

(MLBAM) mlbam_id: 682985
(Baseball-Reference) bref_id: greenri03
(Retrosheet) retro_id: greer003
(FanGraphs) fangraphs_id: 25976
```

```sh
python scripts/reverse_lookup.py 682985

First Name: Riley
Last Name: Greene
(MLBAM) mlbam_id: 682985
(Baseball-Reference) bref_id: greenri03
(Retrosheet) retro_id: greer003
(FanGraphs) fangraphs_id: 25976
```

## Script Details
The scripts read the combined CSV file located at mlb-player-lookup/data/combined_people.csv. The player_lookup.py script looks up the player by their full name, while the reverse_lookup.py script looks up the player by their MLBAM ID. If the player is found, it prints their MLBAM, Baseball Reference, Retrosheet, and FanGraphs IDs. If the player is not found, it suggests possible matches based on the last name or ID.

### Functions
 * lookup_player(full_name, csv_file_path):<br/>
    Looks up a player by their full name in the specified CSV file.
 * reverse_lookup(player_id, csv_file_path):<br/>
    Looks up a player by their player ID in the specified CSV file.
  
Command Line Arguments<br/>
player_name: Full name of the player to look up.<br/>
player_id: ID of the player to look up.


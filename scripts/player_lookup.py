import pandas as pd
import argparse

def lookup_player(full_name, csv_file_path='./mlb-player-lookup/data/combined_people.csv'):
    # Read the combined CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Create a full_name column by concatenating name_first and name_last
    df['full_name'] = df['name_first'] + ' ' + df['name_last']
    
    # Look up the player by full name
    player_data = df[df['full_name'] == full_name]

    # Look up the player by name_last
    possible_matches = None
    if player_data.empty:
        possible_matches = df[df['name_last'] == full_name].dropna(subset=['name_first', 'name_last'])

    
    # Check if the player was found
    if not player_data.empty:
        return player_data, possible_matches
    else:
        return None, possible_matches

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lookup a player in the combined CSV file.')
    parser.add_argument('player_name', type=str, help='Full name of the player to lookup')
    args = parser.parse_args()

    result, possible_matches = lookup_player(args.player_name)
    
    if isinstance(result, pd.DataFrame) and not result.empty:
        if pd.notna(result['key_mlbam'].values[0]):
            print(f'(MLBAM) mlbam_id: {result['key_mlbam'].values[0].astype(int)}')
        else:
            print('mlb_id: N/A')
        if pd.notna(result['key_bbref'].values[0]):
            print(f'(Baseball-Reference) bref_id: {result['key_bbref'].values[0]}')
        else:
            print('bref_id: N/A')
        if pd.notna(result['key_retro'].values[0]) and result['key_retro'].values[0] != '':
            print(f'(Retrosheet) retro_id: {result['key_retro'].values[0]}')
        else:
            print('retro_id: N/A')
        if pd.notna(result['key_fangraphs'].values[0]):
            print(f'(FanGraphs) fangraphs_id: {result['key_fangraphs'].values[0].astype(int)}')
        else:
            print('fangraphs_id: N/A')
    elif isinstance(possible_matches, pd.DataFrame) and not possible_matches.empty:
        print('Player not found. Did you mean one of the following?')
        for i, row in possible_matches.iterrows():
            print(row['full_name'])
    else:
        print('Player not found. Remember to use the player\'s full name (e.g., "Babe Ruth").')
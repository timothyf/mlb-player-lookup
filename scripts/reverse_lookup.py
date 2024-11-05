import pandas as pd
import argparse

def lookup_player(mlbam_id, csv_file_path='./mlb-player-lookup/data/combined_people.csv'):
    # Read the combined CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Look up the player by mlbam_id
    player_data = df[df['key_mlbam'] == mlbam_id]

    # Check if the player was found
    if not player_data.empty:
        return player_data
    else:
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lookup a player in the combined CSV file.')
    parser.add_argument('mlbam_id', type=int, help='MLBAM ID of the player to lookup')
    args = parser.parse_args()

    result = lookup_player(args.mlbam_id)
    
    if isinstance(result, pd.DataFrame) and not result.empty:
        print('First Name:', result['name_first'].values[0])
        print('Last Name:', result['name_last'].values[0])
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
    else:
        print('Player not found.')

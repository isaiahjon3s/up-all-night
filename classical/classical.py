import pandas as pd
import os

def main():
    # Get the current directory and construct the path to the CSV file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "classical_data.csv")
    
    try:
        # Read the CSV file
        df = pd.read_csv(csv_path)
        
        print("🎼 Classical Music Database")
        print("=" * 50)
        print(f"Total pieces: {len(df)}")
        print("\nColumns:", list(df.columns))
        print("\nFirst 10 pieces:")
        print(df.head(10).to_string(index=False))
        
        print("\n" + "=" * 50)
        print("Pieces by Period:")
        period_counts = df['period'].value_counts()
        for period, count in period_counts.items():
            print(f"  {period}: {count} pieces")
        
        print("\n" + "=" * 50)
        print("Top 10 Composers by Number of Pieces:")
        composer_counts = df['composer'].value_counts().head(10)
        for composer, count in composer_counts.items():
            print(f"  {composer}: {count} pieces")
        
        print("\n" + "=" * 50)
        print("Average Duration by Period:")
        avg_duration = df.groupby('period')['duration_minutes'].mean().round(1)
        for period, avg in avg_duration.items():
            print(f"  {period}: {avg} minutes")
            
        return df
        
    except FileNotFoundError:
        print(f"Error: Could not find the CSV file at {csv_path}")
        return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def search_by_composer(composer_name):
    """Search for pieces by a specific composer"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "classical_data.csv")
    
    try:
        df = pd.read_csv(csv_path)
        matches = df[df['composer'].str.contains(composer_name, case=False, na=False)]
        
        if not matches.empty:
            print(f"\n🎵 Pieces by {composer_name}:")
            print(matches[['piece_title', 'duration_minutes', 'period', 'year_composed']].to_string(index=False))
        else:
            print(f"No pieces found for composer: {composer_name}")
            
    except Exception as e:
        print(f"Error searching: {e}")

def search_by_period(period_name):
    """Search for pieces from a specific period"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "classical_data.csv")
    
    try:
        df = pd.read_csv(csv_path)
        matches = df[df['period'].str.contains(period_name, case=False, na=False)]
        
        if not matches.empty:
            print(f"\n🏛️ {period_name} Period Pieces:")
            print(matches[['piece_title', 'composer', 'duration_minutes', 'year_composed']].to_string(index=False))
        else:
            print(f"No pieces found for period: {period_name}")
            
    except Exception as e:
        print(f"Error searching: {e}")

if __name__ == "__main__":
    main()
    
    # Example searches (uncomment to use)
    # search_by_composer("Beethoven")
    # search_by_period("Baroque")
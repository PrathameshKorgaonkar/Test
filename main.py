import argparse
 
def main():
    parser = argparse.ArgumentParser(description='Process some choices.')
    parser.add_argument('--choices', type=str, required=True, help='Comma-separated choices parameter from Jenkins')
 
    args = parser.parse_args()
 
    # Split the comma-separated string into a list
    choices = args.choices.split(',')
 
    print(f'Selected choices: {choices}')
 
if __name__ == "__main__":
    main()

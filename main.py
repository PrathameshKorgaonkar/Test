import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--jobs')
    args = parser.parse_args()
    jobs = args.choices.split(',')
    print(f'Job Count:{len(jobs)}\nJob Name:{jobs}')

if __name__ == "__main__":
    main()

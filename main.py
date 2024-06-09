import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    parser.add_argument('username')
    parser.add_argument('password')
    parser.add_argument('build_number')
    parser.add_argument('--jobs')
    args = parser.parse_args()
    jobs = args.jobs.split(',')
    print(f'Url:{args.url}')
    print(f'Username:{args.username}')
    print(f'Password:{args.password}')
    print(f'Build Number:{args.build_number}')
    print(f'Job Count:{len(jobs)}\nJob Name:{jobs}')

if __name__ == "__main__":
    main()

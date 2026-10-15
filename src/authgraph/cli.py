import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="authgraph",
        description="Command-line interface for authentication graph analysis.",
    )
    parser.parse_args()


if __name__ == "__main__":
    main()

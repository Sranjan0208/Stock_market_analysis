# src/main.py
from data_collection import collect_data
from data_processing import process_all
from data_analysis import analyze_all
from visualization import visualize_all


def main():
    print("Collecting data...")
    collect_data()

    print("Processing data...")
    process_all()

    print("Running analysis...")
    analyze_all()

    print("Visualizing results...")
    visualize_all()


if __name__ == "__main__":
    main()

# CLI Personal Finance Tracker - Project Overview

## 1. What This Tool Does

This is a basic command-line interface (CLI) tool designed to help users log simple financial transactions into a local CSV file (`finance.csv`). It records four straightforward components—income, expenses, source, and total—allowing users to keep a basic text-based record of their spending directly from the terminal.

---

## 2. Major Components

- **Terminal Input (`argparse`)**: Handles basic command-line flags to capture user inputs for income, expenses, and transaction sources.
- **Previous Balance Retrieval (`get_previous_total`)**: Reads the existing CSV file to fetch the last recorded total so that new entries can calculate the updated balance.
- **Data Logging (`output` & `csv.DictWriter`)**: Appends the new transaction dictionary to the CSV file, writing a header row if the file is completely new or empty.

---

## 3. Learnings Summary

- **CLI Parameter Management**: Covered basic `argparse` setup, including descriptions, flag definitions, and parsing single terminal inputs into an output namespace.
- **Overcoming RAM Volatility**: Addressed why hardcoded script variables reset to zero on restart and how fetching previous states from disk solves this.
- **File Handling & Validation Strategies**: Understood the differences between Reader validation (checking path and empty lists sequentially to prevent crashes) and Writer validation (checking file existence and size concurrently to avoid duplicate headers).

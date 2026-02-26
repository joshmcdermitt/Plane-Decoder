# Plane-Decoder

A Python script that decodes aircraft serial numbers into readable information, designed to automate data entry tasks.

## Features

- **Serial Number Validation**: Ensures serial numbers meet minimum length requirements (8+ characters)
- **Decoding Logic**: Extracts and interprets the following information from serial numbers:
  - Sequence number (first 3 digits)
  - Manufacturing year (2-letter code, where 'AA' = 2016)
  - Manufacturing month (2-digit code, 01-12)
  - Aircraft model (single letter code)
- **Batch Processing**: Reads serial numbers from an input file and saves decoded results to an output file
- **Error Handling**: Comprehensive error handling for invalid formats, missing files, and permission issues

## Supported Models

- `P`: Model 107

## Usage

Run the script interactively:
```bash
python decoder.py
```

The script will prompt for:
1. Input filename containing serial numbers (one per line)
2. Output filename for decoded results

## Serial Number Format

Serial numbers should follow this structure:
- Positions 1-3: Sequence number (numeric)
- Positions 4-5: Year code (letters, e.g., 'AA', 'AB', etc.)
- Positions 6-7: Month code (01-12)
- Position 8: Model code (letter)

Example output format:
```
Sequence Number: 123, Year: 2016, Month: January, Model: Model 107
```

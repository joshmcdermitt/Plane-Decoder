# Base year for 'AA'
BASE_YEAR = 2016
MODEL_CODES = {'P': 'Model 107'}
MONTH_NAMES = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def validate_serial(serial):
    """Validate serial number format"""
    if len(serial) < 8:
        raise ValueError(f"Serial number too short: expected 8+ characters, got {len(serial)}")
    return serial.strip()

def decode_serial(serial):
    """Decode serial number into readable information"""
    try:
        serial = validate_serial(serial)
        
        sequence_number = int(serial[:3])
        year_code = serial[3:5]
        month_code = int(serial[5:7])
        model_code = serial[7]
        
        year_offset = ord(year_code[0]) - ord('A')
        year = BASE_YEAR + year_offset

        month = MONTH_NAMES[month_code - 1] if 1 <= month_code <= 12 else "Unknown Month"
        model = MODEL_CODES.get(model_code, "Unknown Model")

        return f"Sequence Number: {sequence_number}, Year: {year}, Month: {month}, Model: {model}"
    
    except ValueError as e:
        return f"Invalid serial format: {e}"
    except IndexError:
        return "Error: Serial number incomplete or malformed"

if __name__ == "__main__":
    print("Welcome to the Serial Number Decoder")
    readFile = input("Please enter the filename you wish to read from: ")
    outputFile = input("Please enter the filename you wish to save the data to: ")
    
    try:
        # Open output file once, write all results, then close
        with open(readFile, "r") as file, open(outputFile, "w") as output_file:
            for line in file:
                if line.strip():  # Skip empty lines
                    processed_line = decode_serial(line.strip())
                    print(f"Line: {processed_line}")
                    output_file.write(f"Serial Number: {line.strip()} - Decoded Information: {processed_line}\n")
        print(f"Processing complete. Results saved to {outputFile}")
    except FileNotFoundError:
        print(f"Error: Input file '{readFile}' not found.")
    except PermissionError:
        print(f"Error: Permission denied accessing files.")
    except Exception as e:
        print(f"Unexpected error: {e}")

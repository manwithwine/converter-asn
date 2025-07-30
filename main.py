def asdot_to_decimal(asdot):
    try:
        # Ensure the format is standardized with a period separator
        asdot_str = str(asdot).replace(',', '.')
        parts = asdot_str.split('.')
        high = int(parts[0])
        low = int(parts[1])
        asdecimal = high * 65536 + low
        return asdecimal
    except Exception as e:
        print(f"Error converting {asdot}: {e}")
        return None

def convert_asn_file(input_file, output_file):
    # Read the ASDot values from the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Convert each line and store the results
    results = []
    for line in lines:
        asdot = line.strip()  # Remove any whitespace or newline characters
        asdecimal = asdot_to_decimal(asdot)
        if asdecimal is not None:
            results.append(f"{asdot} -> {asdecimal}")

    # Write the converted ASDecimal values to the output file
    with open(output_file, 'w') as file:
        file.write("\n".join(results))

    print(f"Conversion complete. Results saved to {output_file}")

# Example usage
convert_asn_file("data.txt", "result.txt")

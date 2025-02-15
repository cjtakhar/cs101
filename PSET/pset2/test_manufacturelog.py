from manufacturelog import validate_and_extract_log

def run_tests():
    test_cases = [
        # ✅ Valid Cases
        ("B1234PABQ50D20230908", [{'Batch ID': '1234', 'Product Code': 'AB', 'Quantity': 50, 'Date': '20230908'}]),
        ("B9999PZZQ99999999D20991231", [{'Batch ID': '9999', 'Product Code': 'ZZ', 'Quantity': 99999999, 'Date': '20991231'}]),
        ("B1234PABQ0050D20230908", [{'Batch ID': '1234', 'Product Code': 'AB', 'Quantity': 50, 'Date': '20230908'}]),
        ("B1234PABQ50D20230908B5678PXYQ30D20230909", [
            {'Batch ID': '1234', 'Product Code': 'AB', 'Quantity': 50, 'Date': '20230908'},
            {'Batch ID': '5678', 'Product Code': 'XY', 'Quantity': 30, 'Date': '20230909'}
        ]),

        # ❌ Invalid Cases
        ("", "invalid"),  # Empty string
        ("b1234PABQ50D20230908", "invalid"),  # Lowercase 'b'
        ("B123PABQ50D20230908", "invalid"),  # Batch ID too short
        ("B1234P3BQ50D20230908", "invalid"),  # Product Code contains a digit
        ("B1234PABQ50D2023A908", "invalid"),  # Date contains a non-digit
        ("B1234PABQ50D19991231", "invalid"),  # Year below 2000
        ("B1234PABQ50D21000101", "invalid"),  # Year above 2099
        ("B1234PABQ50D20231301", "invalid"),  # Month greater than 12
        ("B1234PABQ50D20230932", "invalid"),  # Day greater than 31
        ("B1234PABQ50D20230908B5678PXYQ0D20230909", "invalid"),  # Quantity is 0
        ("B1234PABQ50D20230908b5678PXYQ30D20230909", "invalid"),  # Second batch lowercase 'b'
        ("B1234PABQ500000000000D20230908", [{'Batch ID': '1234', 'Product Code': 'AB', 'Quantity': 500000000000, 'Date': '20230908'}]),  # Large quantity
        ("B0000PABQ1D20000101", [{'Batch ID': '0000', 'Product Code': 'AB', 'Quantity': 1, 'Date': '20000101'}]),  # Minimum valid values
        ("B1234PABQ50D20230229", [{'Batch ID': '1234', 'Product Code': 'AB', 'Quantity': 50, 'Date': '20230229'}]),  # Leap year ignored
        ("B1234PABQ50D20230908B567PXYQ30D20230909", "invalid"),  # Second batch invalid (Batch ID too short)
        ("B1234PABQ50D20230908B5678PXYQ0030D20230909", [
            {'Batch ID': '1234', 'Product Code': 'AB', 'Quantity': 50, 'Date': '20230908'},
            {'Batch ID': '5678', 'Product Code': 'XY', 'Quantity': 30, 'Date': '20230909'}
        ]),  # Leading zeros in quantity

        # Additional invalid cases
        ("B12X4PABQ50D20230908", "invalid"),  # Batch ID has non-digit
        ("B1234PXYQ50D2023090", "invalid"),  # Date too short
        ("B1234PABQ-50D20230908", "invalid"),  # Quantity negative
        ("B1234PABQ5OD20230908", "invalid"),  # Quantity contains letter
        ("B1234PABQ50D2023AB08", "invalid"),  # Date has letter
        ("B1234PABQ50D20230908B5678PXYQ30D20230909B9876PTWQ25D20231010", [
            {'Batch ID': '1234', 'Product Code': 'AB', 'Quantity': 50, 'Date': '20230908'},
            {'Batch ID': '5678', 'Product Code': 'XY', 'Quantity': 30, 'Date': '20230909'},
            {'Batch ID': '9876', 'Product Code': 'TW', 'Quantity': 25, 'Date': '20231010'}
        ]),  # Three valid batches
        ("B1234PABQ50D20230908 B5678PXYQ30D20230909", "invalid"),  # Space between batches
        ("B1234PABQ50D20230908B5678PXYQ30D2023090", "invalid"),  # Second batch has invalid date
    ]

    passed = 0
    failed = 0

    for i, (test_input, expected) in enumerate(test_cases):
        try:
            result = validate_and_extract_log(test_input)
            if result == expected:
                passed += 1
            else:
                failed += 1
                print(f"❌ Test {i+1} Failed:\n  Input: {test_input}\n  Expected: {expected}\n  Got: {result}\n")
        except Exception as e:
            failed += 1
            print(f"❌ Test {i+1} Error: Exception raised for input {test_input}\n{e}\n")

    print(f"✅ Passed: {passed} / {len(test_cases)}")
    print(f"❌ Failed: {failed} / {len(test_cases)}")

# Run tests only if executed directly
if __name__ == "__main__":
    run_tests()

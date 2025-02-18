# Kuljit Takhar  
# CS101 PSET 2
   
#    Validates and extracts batch manufacturing logs from a given string.
#    A valid batch log follows the format:
#    B####PXXQ###DYYYYMMDD (where # = digits, X = uppercase letters)
    
#   Returns:
#       - A list of dictionaries containing valid batch details if the string is correctly formatted.
#       - "invalid" (string) if the log does not adhere to the format.

# 100/100

def validate_and_extract_log(s):

    batches_info = []
    i = 0
    
    while i < len(s):
        # Ensure batch prefix 'B'
        if s[i] != 'B':
            return "invalid"
        i += 1
        
        # Extract and validate Batch ID (4 digits)
        batch_id = s[i:i+4]
        if len(batch_id) != 4 or not batch_id.isdigit():
            return "invalid"
        i += 4
        
        # Ensure Product Code starts with 'P'
        if i >= len(s) or s[i] != 'P':
            return "invalid"
        i += 1
        
        # Extract and validate Product Code (2 uppercase letters)
        product_code = s[i:i+2]
        if len(product_code) != 2 or not product_code.isalpha() or not product_code.isupper():
            return "invalid"
        i += 2
        
        # Ensure Quantity section starts with 'Q'
        if i >= len(s) or s[i] != 'Q':
            return "invalid"
        i += 1
        
        # Extract Quantity (should be an integer > 0, leading zeros allowed)
        quantity_start = i
        while i < len(s) and s[i].isdigit():
            i += 1
        
        if quantity_start == i:  # No digits found after 'Q'
            return "invalid"
        
        quantity = int(s[quantity_start:i])  # Convert to int to remove leading zeros
        if quantity <= 0:
            return "invalid"
        
        # Ensure Date section starts with 'D'
        if i >= len(s) or s[i] != 'D':
            return "invalid"
        i += 1
        
        # Extract and validate Date (YYYYMMDD format, 8 digits)
        date = s[i:i+8]
        if len(date) != 8 or not date.isdigit():
            return "invalid"
        
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:])
        
        if not (2000 <= year <= 2099):
            return "invalid"
        if not (1 <= month <= 12):
            return "invalid"
        if not (1 <= day <= 31):  # Simplified check as per the specs
            return "invalid"
        
        i += 8  # Move to the next batch
        
        # Store valid batch info
        batches_info.append({
            'Batch ID': batch_id,
            'Product Code': product_code,
            'Quantity': quantity,
            'Date': date
        })
    
    return batches_info if batches_info else "invalid"

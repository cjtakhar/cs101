def validate_and_extract_log(s):
    if s[0] != 'B':
        return "invalid"
    
    batches_info = []
    i = 1

    while i < len(s):
        batch_id = s[i:i+4]
        if len(batch_id) != 4 or not batch_id.isdigit():
            return "invalid"
        i += 4

        if i >= len(s) or s[i] != 'P':
            return "invalid"
        i += 1

        product_code = s[i:i+2]
        if len(product_code) != 2 or not product_code.isalpha() or not product_code.isupper():
            return "invalid"
        i += 2

        if i >= len(s) or s[i] != 'Q':
            return "invalid"
        i += 1

        quantity_start = i
        while i < len(s) and s[i].isdigit():
            i += 1
        
        if quantity_start == i:
            return "invalid"
        
        if i >= len(s) and s[i] != 'D':
            return "invalid"
        i += 1

        date = s[i:i+8]
        if len(date) != 8 or not date.isdigit():
            return "invalid"
        year = int(date[:4])
        if year < 2000 or year > 2099:
            return "invalid"
        month = int(date[4:6])
        if month < 1 or month > 12:
            return "invalid"
        day = int(date[6:])
        if day < 1 or day > 31:
            return "invalid"
        
        quantity = int(s[quantity_start:i])

        if quantity == 0:
            return "invalid"
        
        batches_info.append({
            'Batch ID': batch_id, 
            'Product Code': product_code, 
            'Quantity': quantity, 
            'Date': date
        })

    return batches_info
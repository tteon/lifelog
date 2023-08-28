def unixtime_to_date(unix_timestamp):
    """Converts a Unix timestamp to a human-readable date."""
    return datetime.datetime.fromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')

def extract_number_from_string(string):
    """
    Extracts a number from a string using regular expressions.
    Returns the extracted number as a string.
    """
    pattern = r"/(\d+)/\d+_label.csv$"
    match = re.search(pattern, string)
    if match:
        return match.group(1)
    else:
        return None
    
def applyint(df:pd.DataFrame,column:str):
    return df[column].apply(lambda x : int(x))
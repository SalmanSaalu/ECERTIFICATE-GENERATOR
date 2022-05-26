import json
import requests
def ppt2pdf(input_file_path,nn):
    headers = {"Authorization": "Bearer ya29.a0ARrdaM9D-jXhIfJ6I53jB6K0RIdwIaSJs3GQXlH0clvOpbTQF0NqMKvbmcL63xbNkZyLAm6FyFBDDGGn7EsF8hTR8VYCauXDRSAw1JfnR_RR94AAGdbvZMpLo66rF9SJBxHjTNVMVFPzGqUUapwRpqTAtFG7"}

    para = {
        "name": nn,
        "parents":["1sJvGmlZfUMCqAL7Oqrsx6DUBDp-KKqKY"]
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open(input_file_path, "rb")
    }

    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )
    
    fi = r.text.split()
    
    st = fi[4]
    st = st[1:-2] 
    
    return st

#

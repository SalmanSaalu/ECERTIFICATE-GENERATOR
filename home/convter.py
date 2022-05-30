import json
import requests
def ppt2pdf(input_file_path,nn):
    headers = {"Authorization": "Bearer ya29.a0ARrdaM-EQyTcsXcgYQREbxaD928VgJVgSKgSXgx2bYI4Dq2AXRkyT48alakygEahlIKGjfwuNSQ0LuaV6G2fNO0Yv89En8nBPUoR0qp89nGvZCWng6KTcLycHKVX1Wi2Icxt7eMBEFj806f9EVv_X1aEMlRX"}

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

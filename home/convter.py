import json
import requests
def ppt2pdf(input_file_path,nn):
    headers = {"Authorization": "Bearer ya29.a0ARrdaM-R_-D13Qqbeao9mZDV8iUM3FEKYbpWw7vFqjJyKGQpeAvZkBcnQlwwBueaU8IFdclaICCtU0vsDAJoIFYnEzVql3aKW2Jlx-pXCQy40EsnMnvls0H5ZFevu7H0-h3jfdvUjdeGglsM5AJfA2DwvrDM"}

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

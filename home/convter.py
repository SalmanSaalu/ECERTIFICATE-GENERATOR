import json
import requests
def ppt2pdf(input_file_path,nn):
    headers = {"Authorization": "Bearer ya29.a0AVA9y1vkfAXCo361MB2j6WQ-ulXVfn-TiufNGuDaxaMqoEoWSMD38QC-8x2bIsHKwuau_fRmD-6Ah_qOsds2__21vcPADQ1xHKtPvuGfj8udbwp77YWq0WgyDZ6dDE0uNCTueg7qInN2uMA0MEeVQQX3NdGSaCgYKATASAQASFQE65dr8cwb2qzgJNJqtU7J3aXaC3w0163"}

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



from requests import request

def parse_raw(raw_path):
    """
    Parsed Returns data needed to make request and even call to request itself for the lazy
    """
    lines = []
    with open(raw_path) as f:
        lines = f.readlines()

    headers = {} #Header stored here in dictionary format so it's easy to to use in 'requests'
    body = "" #Body is saved as a string
    method = None
    url = None

    header_is_finished = False
    first_body_line = True
    line_number = 1

    for line in lines:
        if not line.strip():    #Checks if current line is empty to know where is the end of header/start of body
            header_is_finished = True   #A way to know if header is finished

        elif line_number == 1:  #If it's the first line we get request url and method
            rmethod = line.split(" ")
            method = rmethod[0]
            url = rmethod[1]

        elif not header_is_finished:    #Check if still header
            key, value = line.split(':', 1)
            headers.update({key.strip() : value.strip() })

        elif header_is_finished:    #If header part of the request is finished that means it's time for BODY
            parsedb = line.strip()
            if first_body_line:
                body = parsedb
                first_body_line = False
            else:
<<<<<<< HEAD:raw_requests.py
                body = "{}\n{}".format(body, parsedb)

=======
                body = "\n{}{}".format(body, parsedb)
>>>>>>> 00f700ab24bbc228b82475a2c5f529860c5578ef:raw_requests.py

        line_number += 1

    return {
        'headers' : headers,
        'url' : url,
        'method' : method,
        'body' : body,
        '_request' : lambda: request(method=method, url=url, data=body,headers=headers)
    }

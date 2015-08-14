# RawRequests

Simple and shitty script to parse raw http requests, best suited for "requests" library. Started out in python less that few months ago so don't be too harsh.

    import requests
    
    from raw_requests import parse_raw
    
    parsed = parse_raw('path_to_request_template.txt')
    
    #Manually create the request
    headers = parsed['headers']
    body = parsed['body'] 
    url = parsed['url'] 
    method = parsed['method'] #http request method
    requests.request(method=method, url=url, data=body,headers=headers)
		
    #Or just use exact copy from the raw request
    req = parsed['request']() #executes same request as in the submitted raw

# RawRequests

Simple and shitty script to parse raw http requests, best suited for "requests" library. Started out in python less that few months ago so don't be too harsh.

    import requests
    
    parse = parseraw('path_to_path_of_RawRequest.txt')
    
    #Manually create the request
    headers = parse['headers'] #headers of the request in dictionary because of that can be easly used to create request
    body = parse['body'] #body of the request
    url = parse['url'] #url for the request
    method = parse['method'] #http request method
    request(method=method, url=url, data=body,headers=headers)
		
    #Or just use excat copy from the raw request
    req = raw['request']() #executes same request as in the submitted raw

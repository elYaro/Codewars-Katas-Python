'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''

def domain_name(url):
    print(url)
    if "www" in url:
        url = url.split(".")
        return url[1]
    elif "http" in url:
        url = url.split("//")
        url = url[1].split(".")
        return url[0]
import requests


response= requests.post("https://rankpedict-nxlb6twtva-as.a.run.app",
                    json={"text": "western denim black jeans color "})


print(response.json())

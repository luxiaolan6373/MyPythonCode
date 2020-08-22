import requests

headers={'referer': 'https://music.163.com/search/',
        'pragma': 'no-cache',
        'origin': 'https://music.163.com',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
         }
data={"params":'R5L0obSPbEERifQi4fMcCgukFEI0GoEKn9edzAu0dpEH3NudJyXgsFJL1CwvoVVyFj3BsX/x6jAB/94Rmqli/J/M5WaYP5Oc/AduTza56uD+m3TTMX+fVmWUCdOhUva2',
     'encSecKey': '40a971f759e527679809a687590b7a255ed0bc08fedc8a9167f5eeff44f8bc6b45bba3ddc2df75c5827dc9ca7dd7825e6a26568450fccde187573bfd5857dd9da12e4942fe819aaa6400577fc118177ae41f75378959e775893ce9f51e308d23126326b3a397418e227863bca44afc2ce43b964a0fbb75da14d5875f51a06937'}

res=requests.get('https://music.163.com/weapi/cloudsearch/get/web?csrf_token=',headers=headers,data=data)
print(res.text)
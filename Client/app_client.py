import requests
import json

link = 'http://localhost:8081/users'

tekst= { "ime": "Pera",
         "prezime": "Pirker",
         "username": "ppirker@gmail.com",
         "smer": "RI",
         "predmeti" : [
         {"ime": "Engleski", "espb": 8},
          {"ime": "Elektronika", "espb": 6},
           {"ime": "Bezbenost mreza", "espb": 8}
         ]
}
xroot=requests.post(link,json=tekst)

import httpx

# This is the equivalent of a CURL request from the command line:
# curl -X POST -H "Content-Type: application/json" \
#   -d '{"name":"Myster","email":"mst3k@virginia.edu"}' \
#   http://localhost:8000/people

person = {'name': 'My Name', 'email': 'abc123@virginia.edu'}

response = httpx.post('http://127.0.0.1:80/people', json=person)
print(response.json())

print("Getting people")
response = httpx.get('http://localhost:80/people')
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)
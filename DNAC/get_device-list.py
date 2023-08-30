#!/usr/bin/env python3

import requests
import json

requests.packages.urllib3.disable_warnings()

url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGVjNGU0ZjRjYTdmOTIyMmM4MmRhNjYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4ZSJdLCJ0ZW5hbnRJZCI6IjVlOGU4OTZlNGQ0YWRkMDBjYTJiNjQ4NyIsImV4cCI6MTY1NjI0MjI3OCwiaWF0IjoxNjU2MjM4Njc4LCJqdGkiOiI2NjkyODQ3NC0yZWZhLTQ4YTMtOTQwYS1kY2FjZTcyNmYwYmEiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.qyQCg287HD9g654VExFleUrolS0qDsR_P3THNapnGbZpZyyZgq6NUUu1X_1oAPV5HVe2bweOnQQVcpSnsiZ5yr-m1lPqm0lR2WshZAEX2T-nu1AIOPjuBzw55jTwcxu-ofq7AIsZZoiSl3AhVlTdHNoL8cZxN8auLt3xYB3OrAEZIuTbTmkwamKTWhJ82RmhMMxwDxa_uJbHE2QE_r4PvMquMjSl-vh9J7LBP9J9IHz3Qgy2D6hF9Q8v6-YEpcTL64W3-ARbSZBs_OEoLguPXkNqMCQ0LwXplo1D6v7T28bZlppOGWKG4qxMWIuYMND1CoyxZYtdtd8NQ5UbUQnX4Q"
}

response = requests.get(url, headers=headers, verify=False).json()
data = json.dumps(response, indent=4)

print(data)
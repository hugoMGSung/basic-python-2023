from urllib.parse import urlencode, unquote
import requests
import json

url = "https://apis.data.go.kr/6260000/BusanTblBusinfoeqStusService/getTblBusinfoeqStusInfo"
queryString = "?" + urlencode(
{
  "serviceKey": "JzmUY2JqiPqaZHmZ7VDke8wMFu3m/CXZSUCawmglK99g1cw5ytYYWZ/4VmiJz2Wn5MB1aBEA7N0YlXlJz+/K8A==",
  "numOfRows": "10",
  "pageNo": 1,
  "resultType": "json",
  "stationLoc": "롯데백화점"
}
)
queryURL = url + queryString
response = requests.get(queryURL, verify=False)
print("=== response json data start ===")
print(response.text)
print("=== response json data end ===")
print()

# r_dict = json.loads(response.text)
# r_response = r_dict.get("response")
# r_body = r_response.get("body")
# r_items = r_body.get("items")
# r_item = r_items.get("item")

# result = {}
# for item in r_item:
#         if(item.get("category") == "T1H"):
#                 result = item
#                 break
# for item in r_item:
#         if(item.get("category") == "RN1"):
#                 result2 = item
#                 break

# print("=== response dictionary(python object) data start ===")
# print(result.get("baseTime")[:-2] +" temp : " + result.get("obsrValue") + "C")
# print(result2.get("baseTime")[:-2] +" rain : " + result2.get("obsrValue") + "mm")
# print("=== response dictionary(python object) data end ===")
# print()
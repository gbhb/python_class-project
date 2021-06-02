
import requests

url = "https://hk4e-api-os.mihoyo.com/event/sol/sign?lang=zh-tw"

payload="{\"act_id\":\"e202102251931481\"}"
headers = {
  'Cookie': 'ltuid=7882042; mi18nLang=zh-tw; _ga=GA1.2.1617185233.1614739304; _gid=GA1.2.602457806.1614739304; account_id=7882042; ltoken=eOBajnUi0MiGyXe69vEQ2hnGRzvR8JO4hP6boeSV; cookie_token=T8e45shnxV38WacVRkILLBxytklHbEm14fwf2evS; login_ticket=dQZcgtxmgxIH2WCnR22ixMTVGdYuyC5riNq9HJhd' # 從網站獲得 cookies
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
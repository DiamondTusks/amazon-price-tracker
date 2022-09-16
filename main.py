import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email = ""
password = ""

url = "https://www.amazon.com.au/Instant-Pot-Electric-Functional-Cooker/dp/B08XBZYXQS/ref=d_pd_sbs_sccl_2_5/355-2129324-9301267?pd_rd_w=NfrkV&content-id=amzn1.sym.60409910-add4-4012-8282-3968f35fa8ea&pf_rd_p=60409910-add4-4012-8282-3968f35fa8ea&pf_rd_r=9TR8862R2FCYZGJ341WW&pd_rd_wg=CtSrU&pd_rd_r=d02538e0-ed7c-4e09-9644-585b9b14eac6&pd_rd_i=B08XBZYXQS&th=1"
headers = {
    "Accept_Language":"en-GB,en;q=0.7",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/105.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")
product = soup.find(name="span", id="productTitle").getText()
price = soup.find(name="span", class_="a-price-whole")
rounded_price = round(float(price.getText()))

if rounded_price <= 400:
    message = f"{product} is now only ${rounded_price}!".encode('utf-8')

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="diamondtusks@gmail.com",
            msg=f"Subject:Amazon price Alert!\n\n{message}\n\n{url}",
        )

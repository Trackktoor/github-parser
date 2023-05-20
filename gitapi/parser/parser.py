import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup

github_username = 'Palas1k'
def get_data(url):
    #
    # req = requests.get(url)
    # with open('data/gitdata.html', 'w', encoding="utf-8") as file:
    #     file.write(req.text)

    with open('data/gitdata.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    li_tags = soup.find_all("li", class_='col-12 d-flex flex-justify-between width-full py-4 border-bottom color-border-muted public source')

    project_data = []
    for tag in li_tags:
        rep_title = tag.find("h3", class_="wb-break-all").a.get_text()
        #project_data['title_repository'] = rep_title.strip()
        try:
            rep_description = tag.find("div", class_="col-10 col-lg-9 d-inline-block").p.get_text()
            #project_data['description_repository'] = rep_description
        except:
            rep_description ='Has no description'
        rep_datatime = tag.find("relative-time").get_text('title')
        #date = datetime.strptime(rep_datatime, "%m/%d/%Y")
        rep_urls = "https://github.com" + tag.find("h3", class_ = "wb-break-all").find("a").get("href")
        #project_data['url_repository'] = rep_urls
        project_data.append({
                        "title_repository": rep_title.strip(),
                        "description_repository": rep_description,
                        "last_change_date" : datetime.strptime(rep_datatime,"%b %d, %Y").strftime("%d-%b-%Y"),
                        "url_repository": rep_urls,
                    },
        )
        with open('data/parsed_data.json', 'w', encoding="utf-8") as file:
            json.dump(project_data, file, indent=4, ensure_ascii=False)


get_data( ''.join(f"https://github.com/{github_username}?tab=repositories"))
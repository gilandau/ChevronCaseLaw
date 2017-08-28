from robobrowser import RoboBrowser
import urllib.parse as urlparse
import time
import os
def grab_articles(list_of_cases, target_dir):
    MAIN_URL = "https://scholar.google.com"
    SEARCH_URL = "https://scholar.google.com/scholar?q=&btnG=&hl=en&as_sdt=6%2C39"
    if __name__ == "__main__":
        NO_GO = set([])
        browser = RoboBrowser(user_agent='UPenn Research')
        count = 0
        with open(list_of_cases, "r") as f1:
            for line in f1:
                # case_id = " ".join([line.split(",")][0].split(" ")[:4]).strip()
                case_id = [" " .join(l.split(" ")[:4]).strip() for l in line.split(",")[1:] if ".3d" in l]
                if len(case_id) == 1:
                    new_case_id1 = case_id[0].replace(" ", "_").replace(".", "_").strip()
                    direct = new_case_id1
                else:
                    new_case_id1 = case_id[0].replace(" ", "_").replace(".", "_").strip()
                    new_case_id2 = case_id[1].replace(" ", "_").replace(".", "_").strip()
                    direct = new_case_id1 + "-" + new_case_id2
                if not os.path.exists(os.path.join(target_dir,direct)):
                    os.makedirs(os.path.join(target_dir,direct))
                count = 0
                direct_split = direct.split("-")
                for case in case_id:
                    url_parts = list(urlparse.urlparse(SEARCH_URL))
                    url_args = dict(urlparse.parse_qsl(url_parts[4]))
                    url_args["q"] = case
                    url_parts[4] = urlparse.urlencode(url_args, doseq=True)
                    url = urlparse.urlunparse(url_parts)

                    browser.open(url)
                    print(case_id)
                    print(url)
                    linked_case = browser.find_all(class_="gs_rt")[0].find("a").get("href")
                    browser.open(MAIN_URL + linked_case)


                    current = direct_split[count]
                    directory = os.path.join(os.path.join("Articles",direct), current)

                    with open(directory+".txt", "w", encoding='utf-8') as text, open(directory+"_meta.txt", "w", encoding='utf-8') as meta, open(directory+"_struct.txt","w", encoding='utf-8') as structure:
                        text.write(browser.find(id="gs_opinion").text.strip())

                        cites = browser.find(id="gs_opinion").find_all("a")
                        for c in cites:
                            meta.write(c.text.strip() + "\n")
                        meta.write("##########################################\n")

                        heading = browser.find(id="gs_opinion").find_all("h2")
                        for h in heading:
                            structure.write(h.text.strip() + "\n")

                    count +=1
                time.sleep(45)
if __name__ == "__main__":
    pass
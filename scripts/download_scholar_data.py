from scholarly import scholarly
import json
from datetime import datetime
import os

author: dict = scholarly.search_author_id("Hxf8sNkAAAAJ")
scholarly.fill(author, sections=[
               "basics", "indices", "counts", "publications"])
name = author["name"]
author["updated"] = str(datetime.now())
author["publications"] = {v["author_pub_id"]                          : v for v in author["publications"]}
print(json.dumps(author, indent=2))
os.makedirs("results", exist_ok=True)
with open(f"results/gs_data.json", "w") as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
}

with open(f"results/gs_data_shieldsio.json", "w") as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)

# output each paper subdict to a separate file
for pub_id, pub in author["publications"].items():
    with open(f"results/gs_data_{pub_id}.json", "w") as outfile:
        pub_shieldio_data = {
            "schemaVersion": 1,
            "label": "citations",
            "message": f"{pub['num_citations']}",
        }
        json.dump(pub_shieldio_data, outfile, ensure_ascii=False)


# update ../data/publications.json
with open("../data/publications.json", "r") as infile:
    publications = json.load(infile)

publications["citation_metrics"] = {
    "citations": author["citedby"],
    "h-index": author["hindex"],
    "i10-index": author["i10index"],
    "last_updated": author["updated"][:10],
}

scholar_pubs_cite_dic = {}

for scholar_pub in author["publications"].values():
    title = scholar_pub["bib"]["title"]
    citations = scholar_pub["num_citations"]
    scholar_pubs_cite_dic[title] = citations

scholar_opubs_title_list = list(scholar_pubs_cite_dic.keys())

for pub in publications["publications"]:
    title = pub["title"]
    if title in scholar_opubs_title_list:
        pub["num_citations"] = scholar_pubs_cite_dic[title]

with open("../data/publications.json", "w") as outfile:
    json.dump(publications, outfile, ensure_ascii=False, indent=4)

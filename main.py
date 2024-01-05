import AO3
import csv


with open("origin_fanfiction_recs.csv", 'a', encoding="utf-8", newline='',) as output:
    with open("raw_urls.txt", "r") as urls:
        for url in urls:
            url = url.strip()
            # print(url)
            is_work = url.find('https://archiveofourown.org/works/')
            if is_work >= 0:
                pass
                # try:
                #     workid = AO3.utils.workid_from_url(url)
                #     print(workid)
                #     work = AO3.Work(workid)
                #     if work:
                #         print(f"{work.title=}")
                #         print(f"{work.relationships=}")

                #         csvwriter = csv.writer(output)
                #         csvwriter.writerow([url, work.title, work.relationships, work.rating, work.tags, work.status])
                # except Exception as e:
                #     print(e)                    
            else:
                print(url)

print("All Done!")
print("\a")
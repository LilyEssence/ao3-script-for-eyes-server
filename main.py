import AO3
import csv

#vars
output_file_name = "eyes_fanfiction_recs.csv"
input_file_name = "small_set_urls.txt"

#code
with open(output_file_name, 'a', encoding="utf-8", newline='',) as output_file:
    with open(input_file_name, "r") as urls_file:
        for url in urls_file:
            url = url.strip()
            is_work = url.find('https://archiveofourown.org/works/') >= 0
            if is_work:
                # pass
                try:
                    workid = AO3.utils.workid_from_url(url)
                    work = AO3.Work(workid)
                    if work:
                        csvwriter = csv.writer(output_file)
                        csvwriter.writerow([url, work.title, work.relationships, work.rating, work.tags, work.status])
                except Exception as e:
                    print(e)                    
            else:
                print("Not work: {url}")

print("All Done!")

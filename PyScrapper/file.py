import csv

# Comma Seperated Values (csv)


def save_to_file(jobs):
    with open("job.csv", mode="w", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["title", "company", "location", "link"])

        for job in jobs:
            writer.writerow(list(job.values()))

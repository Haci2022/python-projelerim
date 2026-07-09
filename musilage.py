import os
import requests

SAVE_DIR = "caulerpa_mucilage_images"
os.makedirs(SAVE_DIR, exist_ok=True)

MAX_IMAGES = 1000
PER_PAGE = 50  # iNaturalist limit

def download_image(url, path):
    try:
        img = requests.get(url, timeout=10)
        if img.status_code == 200:
            with open(path, "wb") as f:
                f.write(img.content)
            return True
    except:
        pass
    return False


def get_inaturalist_images():
    print("[iNaturalist] fetching...")
    page = 1
    count = 0

    while count < MAX_IMAGES:
        url = (
            "https://api.inaturalist.org/v1/observations"
            f"?q=caulerpa+mucilage&per_page={PER_PAGE}&page={page}"
            "&photos=true"
        )

        r = requests.get(url).json()

        if "results" not in r or len(r["results"]) == 0:
            break

        for obs in r["results"]:
            if count >= MAX_IMAGES:
                break

            try:
                photos = obs.get("photos", [])
                if not photos:
                    continue

                img_url = photos[0]["url"].replace("square", "large")
                file_path = os.path.join(SAVE_DIR, f"inat_{count}.jpg")

                if download_image(img_url, file_path):
                    print("Downloaded:", file_path)
                    count += 1
            except:
                continue

        page += 1

    return count


def get_gbif_images():
    print("[GBIF] fetching...")
    offset = 0
    count = 0

    while count < MAX_IMAGES:
        url = (
            "https://api.gbif.org/v1/occurrence/search"
            f"?q=caulerpa&mediaType=StillImage&limit=100&offset={offset}"
        )

        r = requests.get(url).json()

        results = r.get("results", [])
        if not results:
            break

        for item in results:
            if count >= MAX_IMAGES:
                break

            media = item.get("media", [])
            if not media:
                continue

            for m in media:
                if "identifier" in m:
                    img_url = m["identifier"]
                    file_path = os.path.join(SAVE_DIR, f"gbif_{count}.jpg")

                    if download_image(img_url, file_path):
                        print("Downloaded:", file_path)
                        count += 1
                        break

        offset += 100

    return count


if __name__ == "__main__":
    total1 = get_inaturalist_images()
    total2 = get_gbif_images()

    print(f"\nToplam indirilen görsel: {total1 + total2}")
    
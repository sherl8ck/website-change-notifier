from app.config import URLS
from app.scraper import fetch_page, parse_notices
from app.storage import load_data, save_data
from app.detector import is_new_notice
from app.notifier import send_message


def main():
    saved = load_data()

    for faculty, url in URLS.items():

        print(f"\nChecking {faculty}...")

        html = fetch_page(url)
        notices = parse_notices(html)

        if not notices:
            print("No notices found.")
            continue

        latest = notices[0]

        # First run: save the current latest notice without sending a message
        if faculty not in saved:
            saved[faculty] = latest
            print(f"Initialized {faculty}.")
            continue

        if is_new_notice(faculty, latest, saved):

            message = (
                "🎓 University of Allahabad\n\n"
                f"📚 Faculty: {faculty}\n\n"
                f"📅 Date: {latest['date']}\n\n"
                f"📢 Notice:\n{latest['title']}\n\n"
                f"🔗 {latest['link']}"
            )

            send_message(message)

            print(f"✅ New notice sent for {faculty}")

            saved[faculty] = latest

        else:
            print(f"✅ No new notice for {faculty}")

    save_data(saved)


if __name__ == "__main__":
    main()
from utils.file_utils import read_file
from utils.regex_utils import extract_with_regex
from config import LOG_FILE


def display_menu():
    """Afișează meniul interactiv pentru utilizator."""
    print("\nSelectează opțiunea dorită:")
    print("1. Extrage toate reqId-urile din loguri")
    print("2. Extrage toate nivelurile (level)")
    print("3. Extrage toate mesajele")
    print("4. Extrage toate adresele IP (remoteAddr)")
    print("5. Extrage toate userAgent-urile")
    print("6. Extrage toate URL-urile")
    print("7. Filtrează logurile care conțin 'error'")
    print("8. Filtrează logurile cu Login failed")
    print("9. Ieșire")


def main():
    logs = read_file(LOG_FILE)

    while True:
        display_menu()
        choice = input("\nIntrodu o opțiune (1-9): ")

        if choice == "1":
            print("\nExtragem reqId-urile:")
            reqid_pattern = r'"reqId":"([^"]+)"'
            req_ids = [extract_with_regex(reqid_pattern, log) for log in logs]
            for idx, req_id in enumerate(req_ids, start=1):
                if req_id:
                    print(f"{idx}. {req_id[0]}")

        elif choice == "2":
            print("\nExtragem nivelurile (level):")
            level_pattern = r'"level":(\d+)'
            levels = [extract_with_regex(level_pattern, log) for log in logs]
            for idx, level in enumerate(levels, start=1):
                if level:
                    print(f"{idx}. Level {level[0]}")

        elif choice == "3":
            print("\nExtragem mesajele:")
            message_pattern = r'"message":"([^"]+)"'
            messages = [extract_with_regex(message_pattern, log) for log in logs]
            for idx, message in enumerate(messages, start=1):
                if message:
                    print(f"{idx}. {message[0]}")

        elif choice == "4":
            print("\nExtragem adresele IP:")
            ip_pattern = r'"remoteAddr":"([^"]+)"'
            ips = [extract_with_regex(ip_pattern, log) for log in logs]
            for idx, ip in enumerate(ips, start=1):
                if ip:
                    print(f"{idx}. {ip[0]}")

        elif choice == "5":
            print("\nExtragem userAgent-urile:")
            ua_pattern = r'"userAgent":"([^"]+)"'
            user_agents = [extract_with_regex(ua_pattern, log) for log in logs]
            for idx, ua in enumerate(user_agents, start=1):
                if ua:
                    print(f"{idx}. {ua[0]}")

        elif choice == "6":
            print("\nExtragem URL-urile:")
            url_pattern = r'"url":"([^"]+)"'
            urls = [extract_with_regex(url_pattern, log) for log in logs]
            for idx, url in enumerate(urls, start=1):
                if url:
                    print(f"{idx}. {url[0]}")

        elif choice == "7":
            print("\nFiltrăm logurile care conțin 'error':")
            error_logs = [log for log in logs if "error" in log.lower()]
            for idx, log in enumerate(error_logs, start=1):
                print(f"{idx}. {log}")

        elif choice == "8":
            print("\nFiltrăm logurile de tip 'Login failed':")
            login_failed_pattern = r'Login failed: ([^"]+)'
            failed_logs = [extract_with_regex(login_failed_pattern, log) for log in logs]
            for idx, failed in enumerate(failed_logs, start=1):
                if failed:
                    print(f"{idx}. Login failed for user: {failed[0]}")

        elif choice == "9":
            print("\nIeșire din program. La revedere!")
            break

        else:
            print("\nOpțiune invalidă. Te rog să alegi o opțiune între 1 și 9.")


if __name__ == "__main__":
    main()

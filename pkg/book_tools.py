import json


def read_books(file_name: str) -> list:
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 '{file_name}'。")
        raise
    except (json.JSONDecodeError, ValueError) as e:
        print(f"錯誤：'{file_name}' 的 JSON 格式無效 ({e})。")
        raise
    except OSError as e:
        print(f"錯誤：讀取檔案時發生系統錯誤 ({e})。")
        raise


def write_books(books: list, file_name: str) -> None:
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(books, f, ensure_ascii=False, indent=4)
        print(f"成功匯出 {len(books)} 筆書籍資料至 {file_name}。")
    except OSError as e:
        print(f"錯誤：寫入檔案失敗 ({e})。")


def search_books(books: list, keyword: str) -> list:
    kw = keyword.lower()
    return [book for book in books if kw in book["title"].lower()]


def show_books(books: list) -> None:
    if not books:
        print("目前沒有書籍資料。")
        return

    print(f"{'編號':>4}  {'書籍編號':<8}  {'書名':<14}  {'作者':<8}  {'價格':>6}  {'狀態'}")
    for idx, book in enumerate(books, 1):
        status = "已借出" if book["borrowed"] else "可借閱"
        price_str = f"{book['price']:,}"
        print(
            f"{idx:4d}  {book['id']:<6}  {book['title']:<20}  {book['author']:<8}  {price_str:>4}  {status}"
        )
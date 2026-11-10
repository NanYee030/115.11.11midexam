import sys
from pkg.book_tools import read_books, write_books, search_books, show_books

def menu():
    print("\n--- 簡易借書管理系統 ---")
    print("1. 顯示全部書籍")
    print("2. 新增書籍")
    print("3. 查詢書籍")
    print("4. 變更借閱狀態")
    print("5. 顯示最後 3 筆書籍與統計")
    print("6. 匯出書籍資料")
    print("7. 離開系統")
    print("------------------------")

def add_book(books: list):
    while True:
        book_id = input("請輸入書籍編號: ").strip()
        if not book_id:
            print("書籍編號不可為空，請重新輸入。")
            continue
        if any(b["id"] == book_id for b in books):
            print("書籍編號已存在，請重新輸入。")
            continue
        break
    while True:
        title = input("請輸入書名: ").strip()
        if not title:
            print("書名不可為空，請重新輸入。")
            continue
        break
    while True:
        author = input("請輸入作者: ").strip()
        if not author:
            print("作者不可為空，請重新輸入。")
            continue
        break
    while True:
        price_input = input("請輸入價格: ").strip()
        try:
            price = int(price_input)
            if price <= 0:
                print("價格必須為大於 0 的整數，請重新輸入。")
                continue
            break
        except ValueError:
            print("價格必須為大於 0 的整數，請重新輸入。")
    new_book = {
        "id" : book_id,
        "title" : title,
        "author" : author,
        "price" : price,
        "borrowed" : False,
    }
    books.append(new_book)
    print("新增成功。")

def query_books(books: list):
    while True:
        keyword = input("請輸入書名關鍵字: ").strip()
        if not keyword:
            print("關鍵字不可為空，請重新輸入。")
            continue
        break

    results = search_books(books, keyword)
    if not results:
        print("查無符合的書籍。")
    else:
        print("\n--- 查詢結果 ---")
        show_books(results)

def borrow_status(books: list):
    books_id = input("請輸入書籍編號: ").strip()
    target_book = None
    for b in books:
        if b["id"] == books_id:
            target_book = b
            break

    if not  target_book:
        print("查無此書籍編號。")
        return

    target_book["borrowed"] = not target_book["borrowed"]
    new_status = "已借出" if target_book["borrowed"] else "可借閱"
    print(f"「{target_book['title']}」的狀態已變更為: {new_status}")

def show_last_three_and_stats(books: list):
    if not books:
        print("目前沒有書籍資料。")
        return
    print("\n--- 最後 3 筆書籍資料 ---")
    last_three = books[-3:]
    show_books(last_three)

    total_count = len(books)
    borrow_count = sum(1 for b in books if b["borrowed"])
    available_count = total_count - borrow_count
    total_price = sum(b["price"] for b in books)
    avg_price = total_price / total_count

    print("\n--- 統計數據 ---")
    print(f"書籍總數: {total_count}")
    print(f"可借閱數量: {available_count}")
    print(f"已借出數量: {borrow_count}")
    print(f"全部書籍價格合計: {total_price:,}元")
    print(f"平均價格: {avg_price:.2f}元")

def main():
    try:
        books = read_books("books.json")
    except Exception:
        print("程式載入失敗，終止運行。")
        sys.exit(1)

    while True:
        menu()
        choice = input("請選擇功能: ").strip()

        if choice == "1":
            print("\n--- 全部書籍 ---")
            show_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            query_books(books)
        elif choice == "4":
            borrow_status(books)
        elif choice == "5":
            show_last_three_and_stats(books)
        elif choice == "6":
            write_books(books,"output.json")
        elif choice == "7":
            print("系統已退出")
            break
        else:
            print("無效的選項，請輸入 1 ~ 7 之間的數字。")

if __name__ == "__main__":
    main()
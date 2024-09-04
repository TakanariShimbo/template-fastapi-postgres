import httpx

# APIのベースURL
BASE_URL = "http://localhost:18000"  # FastAPIサーバーのアドレスに応じて変更してください


# ユーザー作成
def create_user(name: str):
    url = f"{BASE_URL}/users/create-new-user/"
    payload = {"name": name}
    response = httpx.post(url, json=payload)
    if response.status_code == 200:
        print("ユーザーが作成されました:", response.json())
    else:
        print("ユーザーの作成に失敗しました:", response.status_code, response.json())


# ユーザーIDでユーザーを取得
def get_user_by_id(user_id: int):
    url = f"{BASE_URL}/users/get-user-by-id/{user_id}"
    response = httpx.get(url)
    if response.status_code == 200:
        print("ユーザー情報:", response.json())
    else:
        print("ユーザーの取得に失敗しました:", response.status_code, response.json())


# 名前でユーザーを取得
def get_user_by_name(name: str):
    url = f"{BASE_URL}/users/get-user-by-name/{name}"
    response = httpx.get(url)
    if response.status_code == 200:
        print("ユーザー情報:", response.json())
    else:
        print("ユーザーの取得に失敗しました:", response.status_code, response.json())


# すべてのユーザーを取得
def list_all_users(skip: int = 0, limit: int = 100):
    url = f"{BASE_URL}/users/list-all-users/?skip={skip}&limit={limit}"
    response = httpx.get(url)
    if response.status_code == 200:
        print("すべてのユーザー:", response.json())
    else:
        print("すべてのユーザーの取得に失敗しました:", response.status_code, response.json())


# ユーザーにアイテムを作成
def create_item_for_user(user_id: int, title: str, description: str):
    url = f"{BASE_URL}/users/{user_id}/items/create-item-for-user/"
    payload = {"title": title, "description": description}
    response = httpx.post(url, json=payload)
    if response.status_code == 200:
        print("アイテムが作成されました:", response.json())
    else:
        print("アイテムの作成に失敗しました:", response.status_code, response.json())


# アイテムIDでアイテムを取得
def get_item_by_id(item_id: int):
    url = f"{BASE_URL}/items/get-item-by-id/{item_id}"
    response = httpx.get(url)
    if response.status_code == 200:
        print("アイテム情報:", response.json())
    else:
        print("アイテムの取得に失敗しました:", response.status_code, response.json())


# ユーザーIDでアイテムをリスト表示
def list_items_by_user(user_id: int, skip: int = 0, limit: int = 100):
    url = f"{BASE_URL}/users/{user_id}/items/list-items-by-user/?skip={skip}&limit={limit}"
    response = httpx.get(url)
    if response.status_code == 200:
        print("ユーザーのアイテム:", response.json())
    else:
        print("アイテムの取得に失敗しました:", response.status_code, response.json())


# すべてのアイテムを取得
def list_all_items(skip: int = 0, limit: int = 100):
    url = f"{BASE_URL}/items/list-all-items/?skip={skip}&limit={limit}"
    response = httpx.get(url)
    if response.status_code == 200:
        print("すべてのアイテム:", response.json())
    else:
        print("アイテムの取得に失敗しました:", response.status_code, response.json())


# サンプル実行
if __name__ == "__main__":
    # ユーザーを作成
    create_user("山田 太郎")
    create_user("鈴木 花子")

    # ユーザーIDでユーザーを取得
    get_user_by_id(1)

    # 名前でユーザーを取得
    get_user_by_name("山田 太郎")

    # すべてのユーザーを取得
    list_all_users()

    # ユーザーにアイテムを作成
    create_item_for_user(1, "ペン", "黒いペンです")

    # アイテムIDでアイテムを取得
    get_item_by_id(1)

    # ユーザーIDでアイテムをリスト表示
    list_items_by_user(1)

    # すべてのアイテムを取得
    list_all_items()

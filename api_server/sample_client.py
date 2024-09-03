import httpx

# APIのベースURL
BASE_URL = "http://localhost:18000"


# ユーザー作成
def create_user(name: str):
    url = f"{BASE_URL}/users/"
    payload = {"name": name}
    response = httpx.post(url, json=payload)
    if response.status_code == 200:
        print("User created:", response.json())
    else:
        print("Failed to create user:", response.status_code, response.json())


# ユーザーIDでユーザーを取得
def get_user(user_id: int):
    url = f"{BASE_URL}/users/{user_id}"
    response = httpx.get(url)
    if response.status_code == 200:
        print("User details:", response.json())
    else:
        print("Failed to get user:", response.status_code, response.json())


# すべてのユーザーを取得
def get_users(skip: int = 0, limit: int = 100):
    url = f"{BASE_URL}/users/?skip={skip}&limit={limit}"
    response = httpx.get(url)
    if response.status_code == 200:
        print("All users:", response.json())
    else:
        print("Failed to get users:", response.status_code, response.json())


# ユーザーに関連するアイテムを作成
def create_item_for_user(user_id: int, title: str, description: str):
    url = f"{BASE_URL}/users/{user_id}/items/"
    payload = {"title": title, "description": description}
    response = httpx.post(url, json=payload)
    if response.status_code == 200:
        print("Item created:", response.json())
    else:
        print("Failed to create item:", response.status_code, response.json())


# アイテムIDでアイテムを取得
def get_item(item_id: int):
    url = f"{BASE_URL}/items/{item_id}"
    response = httpx.get(url)
    if response.status_code == 200:
        print("Item details:", response.json())
    else:
        print("Failed to get item:", response.status_code, response.json())


# ユーザーIDで関連するアイテムを取得
def get_items_by_user(user_id: int, skip: int = 0, limit: int = 100):
    url = f"{BASE_URL}/users/{user_id}/items/?skip={skip}&limit={limit}"
    response = httpx.get(url)
    if response.status_code == 200:
        print("Items for user:", response.json())
    else:
        print("Failed to get items:", response.status_code, response.json())


# すべてのアイテムを取得
def get_items(skip: int = 0, limit: int = 100):
    url = f"{BASE_URL}/items/?skip={skip}&limit={limit}"
    response = httpx.get(url)
    if response.status_code == 200:
        print("All items:", response.json())
    else:
        print("Failed to get items:", response.status_code, response.json())


# サンプル実行
if __name__ == "__main__":
    # ユーザー作成
    create_user("John Doe")
    create_user("Jane Doe")

    # ユーザーIDでユーザーを取得
    get_user(1)

    # すべてのユーザーを取得
    get_users()

    # アイテム作成
    create_item_for_user(user_id=1, title="Item 1", description="This is item 1")

    # アイテムIDでアイテムを取得
    get_item(1)

    # ユーザーIDで関連するアイテムを取得
    get_items_by_user(user_id=1)

    # すべてのアイテムを取得
    get_items()

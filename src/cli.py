import click
import requests
import typer
import getpass
import re

app = typer.Typer()

user_bucket_name = "damg-test"
subscription_tiers = ["free", "gold", "platinum"]
BASE_URL = "http://127.0.0.1:8000"
access_token = ""
headers = {"Authorization": f"Bearer {access_token}"}



@app.command("Server_Health")

def health_check():
    # import ipdb ; ipdb.set_trace()

# Prompt the user for server link
    health = typer.prompt("Enter the URL for the Application")

    url= BASE_URL
    url_response= requests.post(url)


    if url_response.status_code == 405:
        typer.echo("Server is up and Running")
    else:
        typer.echo("Internal Server Issue")


@app.command("create_user")
def create_user():
    # Prompt the user for username
    username = typer.prompt("username")
    password = typer.prompt("password")
    password2 =typer.prompt("Reenter password")
    tier = typer.prompt("tier")

    url = "{0}/{1}".format(BASE_URL, "register")

    body = {"username": username, "password": password, "tier": tier}
    username_response = requests.post(url, json=body)

    # typer.echo (username_response.text)
    if username_response.status_code == 201:
        typer.echo("User created")



@app.command("forgot_password")
def create_user():
    # Prompt the user for username
    username = typer.prompt("username")
    password = typer.prompt("password")
    tier = typer.prompt("tier")

    url = "{0}/{1}".format(BASE_URL, "forgot_password")

    body = {"username": username, "password": password, "tier": tier}
    username_response = requests.post(url, json=body)

    # typer.echo (username_response.text)
    if username_response.status_code == 201:
        typer.echo("Password Updated")





@app.command("login")
def user_login():

     # Prompt the user for username
    username = typer.prompt("username")
    password = typer.prompt("password")
    # tier = typer.prompt("tier")

    url = "{0}/{1}".format(BASE_URL, "login")

    response = requests.post(url, json={
        "username": username,
        "password": password
    })

    if response.status_code == 200:
       typer.echo("User Logged in  Successfully")



@app.command("goes_get_year")
def user_login():

     # Prompt the user for Year
    get_year = typer.prompt("Enter The year")
    

    url = "{0}/{1}".format(BASE_URL, "geos_get_year")

    response = requests.get(url)

    if response.status_code == 200:
       typer.echo("The Files has been fetched")


@app.command("get_goes_file_link")
def get_goes_file_link():

    username = typer.prompt("Enter username")
    password = typer.prompt("Enter password")

    url = BASE_URL + "/login"

    response = requests.post(url, json={
        "username": username,
        "password": password
    })

    if response.status_code != 200:
        typer.echo("User not authorized, or invalid credentials!")
        raise typer.Abort()
    
    token = response.json()['token']

    filename = typer.prompt("Enter GOES filename")

    pattern = r"^OR_ABI-L1b-RadC-M6C\d{2}_G\d+_s20\d{12}_e20\d{12}_c20\d{12}\.nc$"

    if not re.match(pattern, filename):
        typer.echo("Enter proper filename")
        typer.Abort()

    fileLinkResponse = requests.get(BASE_URL + f'/get_goes_by_filename/noaa-goes18/{filename}', headers={'Authorization': f'Bearer {token}'})
    
    if fileLinkResponse.status_code == 200:
        typer.echo("AWS File link")
        prefix = "https://damg7245-s3-storage.s3.amazonaws.com/"
        aws_file_link = fileLinkResponse.json()['file_prefix']
        typer.echo(prefix + aws_file_link)
    elif fileLinkResponse.status_code == 429:
        typer.echo("API Calls limit execeeded")
    else:
        typer.echo(fileLinkResponse.json())

@app.command("get_nexrad_file_link")
def get_nexrad_file_link():

    username = typer.prompt("Enter username")
    password = typer.prompt("Enter password")

    url = BASE_URL + "/login"

    response = requests.post(url, json={
        "username": username,
        "password": password
    })

    if response.status_code != 200:
        typer.echo("User not authorized, or invalid credentials!")
        raise typer.Abort()
    
    token = response.json()['token']

    filename = typer.prompt("Enter NEXRAD filename")

    pattern = r'^[A-Z0-9]{4}\d{8}_\d{6}(?:_MDM)?_V\d{2}'

    if not re.match(pattern, filename):
        typer.echo("Enter proper filename")
        typer.Abort()

    fileLinkResponse = requests.get(BASE_URL + f'/get_nexrad_file_link/noaa-nexrad-level2/{filename}', headers={'Authorization': f'Bearer {token}'})

    
    if fileLinkResponse.status_code == 200:
        typer.echo("AWS File link")
        prefix = "https://damg7245-s3-storage.s3.amazonaws.com/"
        aws_file_link = fileLinkResponse.json()['response']
        typer.echo(prefix + aws_file_link)
    elif fileLinkResponse.status_code == 429:
        typer.echo("API Calls limit execeeded")
    else:
        typer.echo(fileLinkResponse.json())




if __name__ == "__main__":
    app() 
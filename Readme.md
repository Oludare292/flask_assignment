### Getting Started with Project Setup

#### Build Docker Image
```sh
sudo docker build -t flask-file-server:latest .
```

#### Run Docker Image

```sh
sudo docker run -d -p 5000:5000 flask-file-server
```

### API DOCUMENT
#### API URL
> http://127.0.0.1:5000/manage_file

> Request Type : POST

### Body

#### Required Params
```sh
"action":String # expected values : read, download
```
#### Optional Params
```sh
"file_name":String # Use this param to save file with custom name 

"url":String #Use this param to perform action on custom file url
```
### Sample Download Action Request

```sh
## Request Body
{
 "action":"download",
 "file_name":"mycustomdownload",
 "url":"https://pastebin.com/raw/PYYBBvEF"
}

## Response
{
    "status": "success",
    "filePath": "/downloads/1623778634.2694185_mycustomdownload.txt"
}
```

### Sample Read Action Request

```sh
## Request Body
{
 "action":"read",
 "url":"https://pastebin.com/raw/PYYBBvEF"
}

## Response
{
    "status": "success",
    "text": "What is Lorem Ipsum?\r\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
}
```

### Error Handlers

#### Invalid Action
```sh
## Request
{
 "action":"xyz"
}

## Response
Response Code : 400
{
    "error": "Invalid action, expected values: read, download"
}
```
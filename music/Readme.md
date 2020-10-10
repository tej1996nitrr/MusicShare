# Query:
query{
  tracks{
    id,
    title,
    description,
    url,
    createdAt
  }
}
o/p:
{
  "data": {
    "tracks": [
      {
        "id": "1",
        "title": "Track1",
        "description": "Track1 desc",
        "url": "Track1 url",
        "createdAt": "2020-06-07T17:06:38.511330+00:00"
      },
      {
        "id": "2",
        "title": "Track2",
        "description": "This is track2",
        "url": "https://track2.com",
        "createdAt": "2020-09-13T06:59:26.944867+00:00"
      }
    ]
  }
}

query{
  track(id:1){
    id,
    description,
    url,
    createdAt,
    title
  }
}
o/p:
{
  "data": {
    "track": {
      "id": "1",
      "description": "Track1 desc",
      "url": "Track1 url",
      "createdAt": "2020-06-07T17:06:38.511330+00:00",
      "title": "Track1"
    }
  }
}
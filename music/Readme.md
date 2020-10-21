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

query{
users{
  email
  username
}
}
o/p
{
  "data": {
    "users": [
      {
        "email": "tejas@gmail.com",
        "username": "tejas"
      },
      {
        "email": "lomdi@gmail.com",
        "username": "lomdi"
      },
      {
        "email": "admin@gmail.com",
        "username": "admin"
      }
    ]
  }
}

query{
  user(id:1){
    email
    username
  }
}
o/p: 
{
  "data": {
    "user": {
      "email": "tejas@gmail.com",
      "username": "tejas"
    }
  }
}

query{
  track(id:1){
    id
    title
    description
    url
  }
}

o/p:
{
  "data": {
    "track": {
      "id": "1",
      "title": "Track1",
      "description": "Track1 desc",
      "url": "Track1 url"
    }
  }
}

# Mutations:
mutation{
  createTrack(description:"desc", title:"Track3", url:"url"){
    track{
      title
      url
      description
    }
  }
}
o/p:
{
  "data": {
    "tracks": [
      {
        "id": "1",
        "title": "Track1",
        "description": "Track1 desc"
      },]
}}

mutation{
  createUser(username:"newUser", password:"password",email:"u@gmail.com")
  {
    user{
      username
      id
    }
  }
}

o/p:
{
  "data": {
    "createUser": {
      "user": {
        "username": "newUser",
        "id": "4"
      }
    }
  }
}
query{
  me{
    id
    username
  }
}
o/p:
{
  "errors": [
    {
      "message": "Not Logged In.!",
      "locations": [
        {
          "line": 81,
          "column": 3
        }
      ],
      "path": [
        "me"
      ]
    }
  ],
  "data": {
    "me": null
  }
}

mutation{
  tokenAuth(username:"admin", password:"admin"){
    token
  }
}
o/p:

{
  "data": {
    "tokenAuth": {
      "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjAzMjg1MzM1LCJvcmlnSWF0IjoxNjAzMjg1MDM1fQ.BUZ6d-TqK31oxOYUuS2-CFxcjiWKDwB5rjNhxdIh7I8"
    }
  }
}

Add header: Authorization and value: JWT `token` and rerun above query
o/p:
{
  "data": {
    "me": {
      "id": "3",
      "username": "admin"
    }
  }
}

mutation{
  createTrack(description:"dec",title:"Title4",url:"google.com"){
    track{
      id
      title
      description
      postedBy{
        username
      }
      
    }
    
  }
}
(Along with auth header and jwt token)
o/p:
{
  "data": {
    "createTrack": {
      "track": {
        "id": "5",
        "title": "Title4",
        "description": "dec",
        "postedBy": {
          "username": "admin"
        }
      }
    }
  }
}

#updateTrack
(logged in with user that created trackId=5)
 mutation{
  updateTrack(trackId:5, title:"Track5", description:"desc", url:"http://track5.com"){
    track{
      id
      title
      description
      url
    }
  }
}

o/p:
{
  "data": {
    "updateTrack": {
      "track": {
        "id": "5",
        "title": "Track5",
        "description": "desc",
        "url": "http://track5.com"
      }
    }
  }
}
If logged in by different user:
{
  "errors": [
    {
      "message": "Not permitted to update this track.",
      "locations": [
        {
          "line": 42,
          "column": 3
        }
      ],
      "path": [
        "updateTrack"
      ]
    }
  ],
  "data": {
    "updateTrack": null
  }
}

mutation{
  deleteTrack(trackId:1){
    trackId
  }
}
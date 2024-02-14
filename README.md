# Django GraphQL Learning Project

This project is created for learning purposes and demonstrates the integration of Django with GraphQL using `django-graphql-jwt`, `graphene`, and `django-filter`.

## Features

- User authentication and authorization with JWT tokens using `django-graphql-jwt`.
- Implementation of GraphQL queries, mutations, and filters using `graphene`.
- Integration of Django ORM with GraphQL using `graphene-django`.
- Filtering of query results using `django-filter`.

## Requirements

- Python 3.x
- Django
- graphene-django
- django-graphql-jwt
- django-filter

## Installation

1. Clone the repository:

```bash
git clone https://github.com/vishalyadav28/news_project.git
```

2. Install dependencies:
```
cd hackernews   
#hehehehe
pip install -r requirements.txt
```

3. Run the development server:
```bash
python manage.py runserver
```

### Usage
- Create a user account using the /graphql endpoint.
- Authenticate the user to obtain a JWT token.
- Use the token for further authenticated requests.
- Access GraphQL queries and mutations through the /graphql endpoint.

## Project structure
```

│
├── hackernews/              # Django project directory
│   ├── users/              # Django app directory
│   │   ├── migrations/     # Database migrations
│   │   ├── schema.py       # GraphQL schema definitions
│   │   ├── models.py       # Django models
│   │   ├── ...
│   ├── links/              # Django app directory
│   │   ├── migrations/     # Database migrations
│   │   ├── schema.py       # GraphQL schema definitions
│   │   ├── models.py       # Django models
│   │   ├── ...
│   │
│   ├── hackernews/          # Django project settings
│   │   ├── settings.py     # Project settings file
│   │   ├── urls.py         # URL configuration
│   │   ├── ...
│   │
│   └── manage.py           # Django project management script
│   └── requirements.txt        # Project dependencies
│
└── README.md               # Project README file
```


```

# query {
# 	votes{
# 		id
# 	}
# }



#user auth


# mutation{ tokenAuth(username:"admin",password:"admin"){ token } }



#create vote

# mutation{
#   createVote(linkId: 1){
#     user{
#       id username email
#     }
#     link{
#       id url description
#     }
#   }
# }


#now check votes on links

# query {
# 	votes{
# 		id
# 		user{
# 			id
# 			username
# 		}
# 		link{
# 			url
# 			description
# 			id
# 		}
# 	}
# }


#check votes by user on link

# query {
# 	links{
# 		url
# 		description
# 		votes{
# 			user{
# 				id
# 				username
# 			}
# 		}
# 	}
# }

#check votes on specific link

# search for link

# query {
# 	links(search: "url",first: 1 ){
# 		id url description
# 	}
# }


#relay edges node


# query{
# 	relayLinks{
# 		edges{
# 			node{
# 				id url description
# 				votes{
# 					edges{
# 						node{
# 							id user{
# 								id
# 							}
# 						}
# 					}
# 				}
# 			}
# 		}
# 	}
# }


#pagination

# query {
# 	relayLinks(first: 1){
# 		edges{
# 			node{
# 				id url description
# 			}
# 		}
# 		pageInfo{
# 			startCursor
# 			hasNextPage
# 			endCursor
# 		}
# 	}
# }


# search only using id

# query {
#   relayLinks(id: 1) {
#     edges {
#       node {
#         id
#         url
#         description
#       }
#     }
#   }
# }


#mutation using relay

mutation {
	relayCreateLink(input: {
		url:"https://google.com",
		description:"google search engine"
	})
	{
		link{
			id url description
		}
	}
}
```

### suggestions are appreciated..............keep coding
 




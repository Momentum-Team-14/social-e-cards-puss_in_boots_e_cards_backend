
# Team Puss In Boots Backend

This a an API to store data for ecards that users can create, view, and add comments 

## API Endpoint Reference

Root URL: https://powerful-island-75819.herokuapp.com

| Method | URL  | Description |
| :-------- | :------- | :------------------------- |
| `GET` | /ecard/ | List of all cards |
| `GET` | /ecard/<pk>/ |  Detail for one card|
| `GET` | /comments/<pk> |  Detail for one comment|
| `GET` | /ecard/user/ |  List all of  current users cards|
| `GET` | /comments/user/|  List all of current users comments|
| `POST` | /ecard/ | Add a new ecard |
| `POST` | /comments/ | Add a new comment |
| `POST` | /styles/ | Add a new style for a card |
| `POST` | /auth/users/ | Create a new user |
| `POST` | /styles/ | Add a new style for a card |
| `POST` | /auth/users/ | Create a new user |
| `POST` | /auth/token/login/ | User login |
| `POST` | /auth/token/logout/ | User logout |
| `PATCH` | /ecard/<pk>/ | Update an existing ecard |
| `PATCH` | /comments/<pk>/ | Update an existing comment |
| `DELETE` | /ecard/<pk>/ | Delete a card  |
| `DELETE` | /comments/<pk>/ | Delete a comment  |
|




## Authors

- [@ajsteph89](https://www.github.com/ajsteph89)


## Installation

Once this repo has been cloned, use pipenv to install all of the necessary dependencies from the Pipfile. 

```bash
pipenv install 
```






# Team Puss In Boots Backend

This a an API to store data for ecards that users can create, view, and add comments 

## API Endpoint Reference

Root URL: https://powerful-island-75819.herokuapp.com

| Method | URL  | Description |
| :-------- | :------- | :------------------------- |
| `GET` | /ecard/ | List of all cards |
| `GET` | /ecard/int:pk/ |  Detail for one card|
| `GET` | /comments/int:pk/ |  Detail for one comment|
| `GET` | /ecard/user/int:pk/ |  List all of  current users cards|
| `GET` | /comments/user/|  List all of current users comments|
| `GET` | /following/|  List all of users followed|
| `POST` | /ecard/ | Add a new ecard |
| `POST` | /comments/ | Add a new comment |
| `POST` | /styles/ | Add a new style for a card |
| `POST` | /auth/users/ | Create a new user |
| `POST` | /styles/ | Add a new style for a card |
| `POST` | /auth/users/ | Create a new user |
| `POST` | /auth/token/login/ | User login |
| `POST` | /auth/token/logout/ | User logout |
| `POST` | /following/ | Follow another user|
| `PATCH` | /ecard/int:pk/ | Update an existing ecard |
| `PATCH` | /comments/int:pk/ | Update an existing comment |
| `DELETE` | /ecard/int:pk/ | Delete a card  |
| `DELETE` | /comments/int:pk/ | Delete a comment  |
| `DELETE` | /following/int:pk/ | Remove a user from users follow list|




## Authors

- [@ajsteph89](https://www.github.com/ajsteph89)


## Installation

Once this repo has been cloned, use pipenv to install all of the necessary dependencies from the Pipfile. 

```bash
pipenv install 
```





# 📰 BlogRest
BlogRest is a Django-based backend for a blog application. It provides a RESTful API for managing posts, comments, and user authentication. Built using Django REST Framework, it supports secure login, registration, and administrative control through the Django admin panel.

## 🚀 Features
> - Create and manage blog posts via API
>   
> - Comment system with author linking
>   
> - User registration and token-based authentication
>   
> - Secure login system
>   
> - Django admin for managing posts, comments, and users
>   
> - Testing framework included

## 🧰 Tech Stack
> - Backend:
>   - Python 3.11
>   - Django
>   - Django Rest Framework
>
> - Database: 
>   - PostgreSQL
>
> - Auth:
>   - Token-based authentication using DRF
>
> - Tools:
>   - Docker
>   - Git
>   - unittest


## 📁 Project Structure
```bash
BlogRest/
├── blog/               # Post and comment models, views, serializers
├── users/              # Custom user model and auth endpoints
├── config/             # Project settings and URLs
├── templates/          # Admin and auth templates 
├── static/             # Static assets 
├── manage.py           # Django project manager
└── requirements.txt    # Dependencies
```

## ⚙️ Installation
### 💻 Local Development

#### Clone the Repository:
```bash
git clone https://github.com/xinis002/BlogRest.git
```

#### Navigate to the Project Directory:
```bash
cd BlogRest
```

#### Create and Activate a Virtual Environment:
##### Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
##### Windows
```bash
python3 -m venv venv
venv\Scripts\activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Apply Migrations
```bash
python manage.py migrate
```

#### Create Superuser
```bash
python manage.py createsuperuser
```

#### Run the server 
```bash
python manage.py runserver
```

## 🔐 Authentication
The project uses Token Authentication from Django REST Framework.
- Obtain a token by logging in via ```/api/token/```
- Add the token to your request headers:
```bash
Authorization: Token your_token_here
```




## 🤝 Contributing
> Contributions are welcome! 
> Please fork the repository and submit a pull request with your changes.
> 1. Fork the repository
> 2. Create a new branch ```git checkout -b feature-name```
> 3. Commit your changes
> 4. Push to your fork
> 5. Open a pull request


## 📝 License
This project is open-source and available under the MIT License.














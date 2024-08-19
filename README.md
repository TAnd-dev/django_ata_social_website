# Django Social Media Project

This project is a Django-based web application that allows users to register, log in, manage profiles, and interact with images through actions such as bookmarking and liking. The project also includes features for viewing user activity and image rankings.

## Features

### User Accounts
- **User Registration**: New users can register by providing basic details like username, email, and password.
- **User Login**: Registered users can log in using their credentials.
- **Dashboard**: After logging in, users can view recent activities related to the people they follow.
- **Profile Management**: Users can edit their profile details, including first name, last name, email, date of birth, and profile picture.
- **User List and Detail View**: Users can view a list of all registered users and click on a username to see detailed information about that user.
- **Follow/Unfollow Users**: Users can follow or unfollow other users, and this action is recorded in the activity stream.

### Image Management
- **Image Creation**: Users can bookmark images by providing an image URL and a title.
- **Image Detail View**: Each image has its own detail page, where users can see the total number of views the image has received.
- **Image Liking**: Users can like or unlike images, and this action is recorded in the activity stream.
- **Image Ranking**: A ranking page is available where users can view the most viewed images.
- **Paginated Image List**: Images are displayed in a paginated list, with the option to view the list in an image-only format.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/TAnd-dev/django_ata_social_website.git
    cd django_ata_social_website
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (admin user):**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    Open a web browser and go to `http://127.0.0.1:8000/`.

## Configuration

### Redis Setup
This project uses Redis for caching and storing image ranking data.

- **Install Redis:**
    Follow the instructions on the [official Redis website](https://redis.io/download) to install Redis on your system.

- **Configure Redis in Django:**
    Make sure the Redis server is running and configure the following settings in your `settings.py`:

    ```python
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0
    ```

### Environment Variables
You may need to set up the following environment variables in your `.env` file:

- `SECRET_KEY`: Django secret key.
- `DEBUG`: Set to `True` for development.
- `ALLOWED_HOSTS`: Hosts/domain names that are valid for this site.

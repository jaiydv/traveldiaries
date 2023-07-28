# TravelDiaries - Blogging Website


TravelDiaries is a full-fledged blogging website built using Python, Django, SQLite, HTML, CSS,Bootstrap and JavaScript. The platform allows travelers to share their exciting adventures and travel experiences with the world. This repository contains the source code and resources required to set up and run the TravelDiaries website.

## Features

- **Blogging Made Easy:** TravelDiaries provides a user-friendly interface with the Froala Editor, empowering users to create and customize their travel blog posts with ease.

- **User Registration and Authentication:** Users can sign up, create accounts, and log in securely. Account verification is achieved through email verification, ensuring a safe and authentic user community.

- **Blog Creation and Management:** Registered users can write, edit, and publish their travel blogs, complete with multimedia content like images and videos.


## Installation and Setup

Follow these steps to set up the TravelDiaries website locally on your machine:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/jaiydv/traveldiaries.git
   ```

2. Navigate to the project directory:
   ```
   cd TravelDiaries
   ```

3. Create a virtual environment (optional but recommended) to isolate project dependencies:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For macOS and Linux:
     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

6. Set up the database:
   ```
   python manage.py migrate
   ```

7. Create a superuser for accessing the Django admin panel:
   ```
   python manage.py createsuperuser
   ```

8. Start the development server:
   ```
   python manage.py runserver
   ```

9. Visit `http://127.0.0.1:8000` in your web browser to access the TravelDiaries website.

## Usage

- To create a new blog, sign up or log in to your account and click on the "Add Blog" button on the dashboard.
- Use the Froala Editor to write your blog content, add images, videos, and other multimedia elements to make your blog engaging.
- Click on the "Create bLog" button to make your blog post visible to other users.

## Contributing

We welcome contributions to enhance the TravelDiaries website. If you discover any bugs, have feature requests, or wish to submit improvements, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name: `git checkout -b feature/your-feature` or `bugfix/issue-description`.
3. Implement your changes and commit them with clear commit messages.
4. Push your changes to your fork: `git push origin feature/your-feature`.
5. Open a pull request (PR) on the main repository, explaining your changes and the problem they address.

## License

TravelDiaries is open-source and licensed under the [MIT License](LICENSE).
## Credits
The template is inspired from the templates of bootstapious.com 

##Contact
If you have any questions or need further assistance, feel free to reach out to our team at jaipywork@gmail.com or by creating an issue on this repository.

Happy blogging and safe travels! 🌍✈️

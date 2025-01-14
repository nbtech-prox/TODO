# Listify+ 📝

A modern, elegant task management system that helps you organize your life with style. Built with Flask and Tailwind CSS, Listify+ offers a seamless experience for managing tasks with advanced features for both users and administrators.

## 🌟 Features

### User Management
- 🔐 Secure authentication system
- 👥 User registration with full name
- 🎭 Role-based access control (Admin/User)
- 📊 Last login tracking
- 🔑 Password hashing for security

### Task Management
- ✅ Create, read, update, and delete tasks
- 🎯 Task prioritization (Low, Medium, High)
- ⏰ Task completion tracking
- 📝 Task descriptions
- 🗂️ Task filtering and ordering

### Admin Features
- 📊 Admin dashboard with system statistics
- 👥 User management
- 📋 View all tasks from all users
- 📈 System monitoring capabilities

### Security Features
- 🔒 CSRF protection
- 🔐 Secure password storage
- 🛡️ Environment-based configuration
- 🔑 Secret key management

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip (Python package manager)
- Git (optional)

### Installation

1. Clone the repository (optional):
```bash
git clone https://github.com/nbtech-prox/TODO.git
cd TODO
```

2. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create environment files:
```bash
# Create .env file with:
FLASK_ENV=development
FLASK_APP=run.py
SECRET_KEY=your-secret-key
WTF_CSRF_SECRET_KEY=your-csrf-key
DATABASE_URL=sqlite:///db.sqlite
```

5. Initialize the database:
```bash
flask init-db
```

6. Run the application:
```bash
flask run
```

The application will be available at `http://localhost:5000`

### Default Admin Account
- Email: admin@example.com
- Password: admin123

## 🏗️ Project Structure

```
TODO/
├── app/                    # Application package
│   ├── __init__.py        # App initialization
│   ├── admin.py           # Admin views
│   ├── auth.py            # Authentication views
│   ├── cli.py             # CLI commands
│   ├── config.py          # Configuration
│   ├── forms.py           # Form classes
│   ├── main.py            # Main views
│   ├── models.py          # Database models
│   ├── static/            # Static files
│   └── templates/         # HTML templates
├── instance/              # Instance-specific files
│   └── db.sqlite          # SQLite database
├── .env                   # Environment variables
├── .env.example           # Example environment file
├── .flaskenv             # Flask configuration
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── requirements.txt      # Python dependencies
└── run.py               # Application entry point
```

## 🔧 Configuration

The application uses a multi-environment configuration system:

- **Development**: Debug enabled, SQLite database
- **Production**: Debug disabled, configurable database
- **Testing**: In-memory SQLite database

Configuration is managed through:
1. `config.py`: Base configuration classes
2. `.env`: Environment-specific settings
3. `.flaskenv`: Flask-specific settings

## 💻 Usage

### User Features
1. Register a new account
2. Login with email and password
3. Create new tasks with priority
4. View and manage your tasks
5. Mark tasks as complete/incomplete
6. Edit or delete your tasks

### Admin Features
1. Access the admin dashboard
2. View system statistics
3. Manage all users
4. View and manage all tasks
5. Monitor system activity

## 🔒 Security

- Passwords are hashed using Werkzeug's security functions
- CSRF protection on all forms
- Environment-based secrets management
- SQL injection protection through SQLAlchemy
- XSS protection through template escaping

## 🛠️ Development

### Adding New Features
1. Create new routes in appropriate blueprints
2. Add models to `models.py` if needed
3. Create forms in `forms.py` if needed
4. Add templates in `templates/`
5. Update tests accordingly

### Database Migrations
The project uses SQLite with SQLAlchemy. To modify the database:

1. Update models in `models.py`
2. Run database initialization:
```bash
flask init-db
```

## 🧪 Testing

Run tests using:
```bash
python -m pytest
```

## 📝 License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0) - see the [LICENSE](LICENSE) file for details.

This means:
- ✅ You can use this code commercially
- ✅ You can modify this code
- ✅ You can distribute this code
- ✅ You can use this code privately
- ✅ You can use patent claims
- ❗ You MUST disclose the source code
- ❗ You MUST state changes to the code
- ❗ You MUST share your modifications under the same license
- ❗ You MUST include the original license
- ❗ You MUST include copyright notices

For more information about GPL-3.0, visit: https://www.gnu.org/licenses/gpl-3.0.en.html

## 👥 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
6. Clicking the star

## 📞 Support

For support, please create an issue in the repository or contact the development team.

## 🙏 Acknowledgments

- Flask framework and extensions
- Tailwind CSS for styling
- All contributors and users

---
Made with ❤️ by Nuno Batista - NBTech

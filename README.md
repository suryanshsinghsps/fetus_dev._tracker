# fetus_dev._tracker
fetus-tracker-python/
│
├── .github/                # GitHub-specific configurations
│   └── workflows/          # Automated testing (CI/CD)
│
├── assets/                 # Non-code resources
│   ├── images/             # Diagrams, app icons, ultrasound placeholders
│   └── reference_data/     # Static JSON/CSV files of weekly milestones
│
├── src/                    # Core Source Code
│   ├── __init__.py         # Makes 'src' a package
│   ├── core/               # Mathematical and medical logic
│   │   ├── calculations.py # Due dates, BMI, growth percentiles
│   │   └── milestones.py   # Weekly development data retrieval
│   ├── database/           # Data persistence
│   │   ├── db_manager.py   # SQLite or PostgreSQL connection logic
│   │   └── models.py       # User and health record data models
│   └── ui/                 # The Interface (Web or Desktop)
│       ├── app.py          # Main Streamlit/Flask/Tkinter entry point
│       └── components.py   # Reusable UI widgets (charts, forms)
│
├── tests/                  # Quality Assurance
│   ├── test_logic.py       # Tests for date calculations
│   └── test_db.py          # Tests for data saving/loading
│
├── .env.example            # Template for environment variables (Secrets)
├── .gitignore              # Tells Git what to ignore (venv, __pycache__)
├── LICENSE                 # Legal permissions (e.g., MIT or GPL)
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
└── setup.py                # Configuration for installing as a package

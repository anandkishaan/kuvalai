# 🌾 Kuvalai - Smart Agricultural Guide System

Kuvalai is a simple and elegant web application to guide farmers or agricultural workers in choosing the correct **crop**, **chemical**, and **sprayer**, and shows dosage instructions with illustrations and multilingual support (English + Tamil).

> Made with ❤️ by [balakumaran1507](https://github.com/balakumaran1507)

---

## 🛠️ Tech Stack

* Python 3.10+
* Flask
* Flask-SQLAlchemy
* HTML/CSS (Jinja templating)
* SQLite (for simplicity)

---

## 📦 Folder Structure

```
kuvalai/
├── app.py                   # Main Flask app
├── kuvalai.db               # Local SQLite DB (auto-generated)
├── .gitignore
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/              # All crop/chemical/sprayer/guide images
├── templates/
│   ├── index.html
│   ├── crop.html
│   ├── chemical.html
│   ├── sprayer.html
│   ├── result.html
│   └── admin.html
└── instance/                # Flask default instance folder (auto-created)
```

---

## 🔧 Prerequisites

* Python 3.10+ installed
* `pip` for managing dependencies
* Git (for cloning)

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/balakumaran1507/kuvalai.git
cd kuvalai
```

### 2. Create virtual environment (recommended)

```bash
python -m venv .venv
source .venv/Scripts/activate  # On Windows
# or
source .venv/bin/activate      # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install flask flask_sqlalchemy
```

### 4. Run the Flask app

```bash
python app.py
```

The app will be available at:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🧑‍🌾 How to Use

### Main Flow

* Visit `/`
* Choose your **Crop** from the list (with image selection)
* Select the **Chemical**
* Choose a **Sprayer**
* View **Dosage Image & Instructions** in English + Tamil

### Admin Panel

Visit:
**[http://127.0.0.1:5000/admin](http://127.0.0.1:5000/admin)**

You can add:

* New Crops
* Chemicals
* Sprayers
* Dosage Guides (link chemical + sprayer combo with dosage image and text)

> Note: Make sure the image files are placed in `static/images/` and match the filenames exactly (e.g., `rice.png`, `cup500.png`)

---

## ❌ Ignored Files

Your `.gitignore` already prevents the following from being committed:

```
kuvalai.db
__pycache__/
*.pyc
instance/
.venv/
```

---

## 📸 Optional: Screenshots

*Add screenshots of the UI for better understanding*

---

## 🧠 Future Plans

* Image upload via admin panel
* Mobile responsive layout
* Multilingual voice instructions
* Export dosage cards as PDF
* User roles (admin/viewer)

---

## 👨‍🏫 License

This project is open-source under the MIT License.

---

**Made with care, culture, and code for our farmers 🌾🇮🇳**

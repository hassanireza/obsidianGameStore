<p align="center">
  <img src="docs/bannergithub.png" width="100%" alt="Obsidian Game Club Banner">
</p>

<h1 align="center">Obsidian Game Club</h1>

<p align="center">
A premium browser gaming platform built with Django, delivering a modern Apple inspired experience through elegant design, seamless gameplay, and scalable architecture.
</p>

<p align="center">

[![CI](https://img.shields.io/github/actions/workflow/status/hassanireza/obsidianGameClub/ci.yml?style=for-the-badge&logo=githubactions&logoColor=white&label=CI)](https://github.com/hassanireza/obsidianGameClub/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Responsive](https://img.shields.io/badge/Responsive-Yes-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-black?style=for-the-badge)

</p>

---

# Overview

Obsidian Game Club is a modern web platform designed for discovering and playing browser based games through a polished and immersive interface. Built on Django, the platform combines elegant UI, scalable architecture, and maintainable code to provide a premium gaming experience for both players and developers.

---

# Features

- Premium Apple inspired interface
- Browser based gameplay
- Responsive design
- User authentication
- Personal game library
- Wishlist management
- Dynamic game catalog
- Django administration panel
- Easily expandable architecture
- Production ready structure

---

# Architecture

```mermaid
flowchart LR

A["🌐 Browser"]
-->B["Django Router"]

B-->C["Authentication"]

B-->D["Game Catalog"]

B-->E["User Library"]

D-->F["Game Engine"]

F-->G["Templates"]

G-->H["HTML • CSS • JavaScript"]
```

---

# User Flow

```mermaid
flowchart TD

A["🏠 Home"]

A-->B["Browse Games"]

B-->C["Game Details"]

C-->D["Play Game"]

D-->E["Save Progress"]

E-->F["Personal Library"]
```

---

# Technology Stack

| Layer | Technology |
|--------|------------|
| Backend | Django |
| Language | Python |
| Frontend | HTML5 |
| Styling | CSS3 |
| Scripting | JavaScript |
| Development | TypeScript |
| Database | SQLite / PostgreSQL |
| Templates | Django Templates |

---

# Project Structure

```text
obsidian_game_club/
│
├── accounts/
├── games/
├── templates/
├── static/
│   ├── css/
│   ├── js/
│   ├── ts/
│   ├── images/
│   └── icons/
├── fixtures/
├── media/
├── config/
├── manage.py
└── requirements.txt
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/obsidian_game_club.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Create an administrator

```bash
python manage.py createsuperuser
```

Start the development server

```bash
python manage.py runserver
```

---

# Deployment

```mermaid
flowchart LR

Developer
-->GitHub

GitHub
-->CI

CI
-->Gunicorn

Gunicorn
-->Django

Django
-->PostgreSQL

Django
-->StaticFiles

StaticFiles
-->CDN
```

---

# Adding New Games

```mermaid
flowchart LR

Assets
-->Register

Register
-->Database

Database
-->CollectStatic

CollectStatic
-->Live
```

1. Add the game assets.
2. Register the game in Django.
3. Upload thumbnails and banners.
4. Collect static files.
5. Launch instantly across the platform.

---

# Production Checklist

- HTTPS enabled
- Environment variables configured
- `DEBUG=False`
- PostgreSQL configured
- Static assets collected
- Media storage configured
- Secure authentication
- Logging enabled
- Scheduled backups

---

# Roadmap

- Multiplayer support
- Achievements
- Leaderboards
- Cloud saves
- User reviews
- Progressive Web App
- Analytics dashboard
- Friends system

---

# License

Distributed under the MIT License.

---

<p align="center">

**Crafted for premium browser gaming experiences.**

Designed with scalability, maintainability, and exceptional user experience at its core.

</p>

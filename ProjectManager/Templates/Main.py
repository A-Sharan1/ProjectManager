import os

# Define your templates dictionary
TEMPLATES = {

    "tkinter":"GUI.py",
    "css": "style.css",
    "html": "index.html",
    "javascript": "script.js",
    "react": "App.js",
    "angular": "app.component.ts",
    "flask": "app.py",
    "django": "manage.py",
    "typescript": "main.ts",
    "java": "Main.java",
    "c": "main.c",
    "cplusplus": "main.cpp",
    "php": "index.php",
    "ruby": "main.rb",
    "swift": "Main.swift",
    "sql": "query.sql",
    "docker": "Dockerfile",
    "git": "gitignore",
    "markdown": "README.md",
    "yaml": "config.yaml",
    "json": "config.json",
    "bash": "script.sh",
    "powershell": "script.ps1",
    "makefile": "Makefile",
    "latex": "main.tex",
    "typescript": "main.ts",
    "html": "index.html",
    "javascript": "script.js",
    "css": "styles.css",
    "react": "App.js",
    "angular": "app.component.ts",
    "vue": "App.vue",
    "flask": "app.py",
    "django": "manage.py",
    "express": "server.js",
    "typescript": "main.ts",
    "java": "Main.java",
    "c": "main.c",
    "cplusplus": "main.cpp",
    "php": "index.php",
    "ruby": "main.rb",
    "swift": "Main.swift",
    "sql": "query.sql",
    "docker": "Dockerfile",
    "git": "gitignore",
    "markdown": "README.md",
    "yaml": "config.yaml",
    "json": "config.json",
    "bash": "script.sh",
    "powershell": "script.ps1",
    "makefile": "Makefile",
    "latex": "main.tex",
}

for i in TEMPLATES:
    with open(os.path.dirname(__file__)+f"/{TEMPLATES[i]}","w"):
        pass
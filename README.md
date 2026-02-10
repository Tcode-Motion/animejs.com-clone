# 🎬 Anime.js - Animation Engine Showcase

> A locally hosted version of the **Anime.js** animation engine website, featuring stunning 3D models, smooth scroll animations, and a comprehensive documentation hub.

![Anime.js](assets/images/anime-js-logo-v4.svg)

---

## 🚀 About This Project

This is a customized local deployment of the [Anime.js](https://animejs.com/) website — a fast, lightweight JavaScript animation library. The project showcases the full power of Anime.js through interactive 3D models, scroll-based animations, and beautifully crafted UI components.

### 👤 Maintained by

**Tanmoy** — Developer focused on Automation, AI, and Innovation.

- 🧠 **Project JARVIS**: Building a personal AI assistant in Python
- 💻 **Stark OS**: Developing a Sci-Fi User Interface for web environments
- 🎨 **3D Visuals**: Creating particle systems using Three.js
- 🛡️ **Security**: Exploring penetration testing with Termux tools

📎 [GitHub Profile](https://github.com/tanmoy44717)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎨 **3D Models** | Interactive GLB models with Draco compression |
| 🌊 **Scroll Animations** | Smooth scroll-triggered reveals and transitions |
| ⚡ **Anime.js v4** | Latest animation engine with Timeline, Stagger, and more |
| 📱 **Responsive** | Works on desktop and mobile browsers |
| 🎯 **Interactive Demos** | Live code examples for every API feature |

---

## 🛠️ Tech Stack

- **Animation Engine**: [Anime.js v4.0.0](https://animejs.com/)
- **3D Rendering**: Three.js with GLTF/GLB + Draco compression
- **Frontend**: Vanilla HTML, CSS, JavaScript
- **Local Server**: Python HTTP Server

---

## 📦 Project Structure

```
animejs.com/
├── index.html                    # Main homepage
├── documentation.html            # API documentation
├── easing-editor.html            # Easing functions editor
├── learn.html                    # Learning resources
├── assets/
│   ├── css/
│   │   └── styles.css            # Main stylesheet
│   ├── js/
│   │   └── scripts.js            # Core JavaScript
│   ├── models/                   # 3D GLB models (22 files)
│   │   ├── module-animate-01.glb
│   │   ├── module-timer-01.glb
│   │   └── ...
│   ├── draco/                    # Draco mesh decoder
│   │   ├── draco_wasm_wrapper.js
│   │   └── draco_decoder.wasm
│   └── images/                   # Static assets
├── sponsors/                     # Sponsor data
└── README.md                     # This file
```

---

## 🏃 Getting Started

### Prerequisites

- Python 3.x (for local server)
- Modern web browser (Chrome, Firefox, Edge)

### Run Locally

```bash
# Clone or download the project
cd animejs.com

# Start the local server
python -m http.server 8000

# Open in browser
# Navigate to http://localhost:8000/index.html
```

> ⚠️ **Important**: You must use a local HTTP server. Opening `index.html` directly via `file://` will cause CORS errors and prevent 3D models from loading.

---

## 📋 API Modules

| Module | Description |
|--------|-------------|
| **Animation** | Core animation API with tweens and keyframes |
| **Timer** | Precise timing controls and callbacks |
| **Timeline** | Sequence and synchronize multiple animations |
| **Stagger** | Create staggered animation effects |
| **Draggable** | Make elements draggable with physics |
| **Scroll** | Scroll-linked animation observer |
| **Scope** | Responsive animations with media queries |
| **SVG** | Animate SVG paths and shapes |
| **Spring** | Physics-based spring animations |
| **WAAPI** | Web Animations API integration |
| **Easings** | 40+ built-in easing functions |

---

## 🙏 Credits

- **Anime.js** by [Julian Garnier](https://github.com/juliangarnier/anime) — Original animation engine
- **Three.js** — 3D rendering engine
- **Draco** — Mesh compression by Google

---

## 📄 License

This project uses Anime.js which is licensed under the [MIT License](https://github.com/juliangarnier/anime/blob/master/LICENSE.md).

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/tanmoy44717">Tanmoy</a>
</p>

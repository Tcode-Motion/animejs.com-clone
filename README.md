# Anime.js v4 - Interactive 3D Showcase

![Anime.js v4 Preview](assets/images/preview.png)

A technical exploration and reconstruction of the **Anime.js v4** landing page, featuring advanced Three.js integrations, modular animation logic, and responsive 3D visualizations.

## 🚀 Key Features

- **Anime.js v4 Engine:** Utilizing the latest modular version of the library.
- **Three.js r172 Integration:** Advanced 3D rendering for the "Animator's Toolbox."
- **Scroll Observer:** Synchronized animations that respond to page scrolling.
- **Scope API:** Responsive and media-query aware animation management.
- **Custom 3D Camera Model:** A high-visibility Three.js camera lens model (added for enhanced visualization).
- **Dynamic Sponsor Loading:** Real-time fetching of GitHub and Platinum sponsors.

## 🛠️ Tech Stack

- **Core:** [Anime.js v4](https://animejs.com)
- **3D Engine:** [Three.js r172](https://threejs.org)
- **Styling:** Custom CSS with CSS Variables for theme management.
- **Assets:** GLB Models, SVG Path animations, and optimized WebP textures.

## 📦 Installation & Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/animejs-v4-showcase.git
   ```

2. **Serve the project:**
   Since the project uses AJAX to load sponsors and GLB models, you must run it through a local server:
   ```bash
   # If you have Python installed
   python -m http.server 8000
   ```

3. **Access the site:**
   Open `http://localhost:8000` in your browser.

## 📂 Project Structure

- `assets/js/scripts.js`: The main logic bundle containing the site engine and Three.js.
- `assets/js/camera-model.js`: Custom 3D interaction layer.
- `assets/models/`: Recovered `.glb` modules for the toolbox visualization.
- `documentation/`: Local copy of the v4 API documentation.

## 🤝 Credits

Original design and library by [Julian Garnier](https://github.com/juliangarnier). Reconstructed and optimized for local analysis.

---
*Generated with ❤️ for technical precision.*
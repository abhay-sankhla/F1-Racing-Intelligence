# 🏎️ Formula 1 Race Intelligence Platform

An interactive Formula 1 data visualization project that combines a custom-designed website with Tableau Public dashboards and stories. The platform presents racing analytics through a modern, F1-inspired interface, making race results, driver performance, constructor standings, and championship trends easier to explore.

## 🌐 Project Links

* **🌍 Live Website:** Add your GitHub Pages URL here after deployment.
* **🎥 Project Explanation Video:** [Watch the Project Explanation](https://cap.scourtfx.info/s/n2qxzm385qpjgd5)
* **📊 Tableau Interactive Dashboard:** [Explore the F1 Dashboard](https://public.tableau.com/views/F1RacingIntelligenceDashboard/Formula1RaceIntelligenceDashboard)
* **🏆 Tableau Championship Story:** [Explore the F1 Story](https://public.tableau.com/views/F1RaceIntelligenceStory/Formula1RaceIntelligenceStory)

## 🎯 Project Objective

The objective of this project is to transform Formula 1 racing data into meaningful visual insights using interactive data visualization.

The project integrates Tableau Public visualizations into a custom website, providing a centralized platform for exploring driver performance, constructor results, circuit analytics, race outcomes, and championship trends.

## ✨ Key Features

### 📊 Interactive Tableau Dashboard

Explore Formula 1 visualizations through an embedded Tableau Public dashboard.

### 🏎️ Driver Performance Analysis

Explore driver results and compare performance indicators available in the dataset.

### 🏁 Constructor Championship Insights

Analyze team results and investigate championship performance trends.

### 🌍 Circuit Analytics

Explore circuit-related data and historical racing patterns represented in the visualizations.

### 📖 Interactive Data Story

Navigate a Tableau Story that presents Formula 1 insights through a sequence of visualizations.

### 🎨 Modern Website Interface

* Dark-themed interface with racing-red accents.
* Formula 1-inspired typography and styling.
* Responsive layout for desktop and mobile screens.
* Navigation links for easy access to project sections.
* Embedded Tableau dashboard and story.

## 🛠️ Technology Stack

| Technology     | Purpose                                         |
| -------------- | ----------------------------------------------- |
| HTML5          | Website structure                               |
| CSS3           | Styling, layout, animations, and responsiveness |
| JavaScript     | Navigation interactions and interface behavior  |
| Tableau Public | Interactive data visualization                  |
| Python         | Local backend experimentation                   |
| Flask          | Optional local web server                       |
| Git & GitHub   | Version control and source code hosting         |
| GitHub Pages   | Static website hosting                          |

## 📁 Project Structure

```text
F1-Racing-Website/
├── index.html
├── app.py
└── README.md
```

* **index.html:** Main website containing the interface and embedded Tableau visualizations.
* **app.py:** Optional Python Flask application for running the website locally.
* **README.md:** Project documentation and setup instructions.

## 🚀 How to Run the Website Locally

### Option 1: Open the HTML Website

1. Download or clone this repository.
2. Open the project folder.
3. Double-click `index.html` to open it in your browser.
4. Ensure you have an internet connection so the Tableau visualizations can load.

### Option 2: Run Using Python Flask

1. Install Python on your computer.

2. Open the project folder in Visual Studio Code.

3. Open the integrated terminal.

4. Install Flask:

   ```bash
   python -m pip install flask
   ```

5. Start the application:

   ```bash
   python app.py
   ```

6. Open the following address in your browser:

   ```text
   http://127.0.0.1:5000
   ```

## 🌐 Deployment

The static website can be published using GitHub Pages.

1. Open the repository on GitHub.
2. Navigate to **Settings → Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**.
4. Choose the `main` branch and the `/ (root)` folder.
5. Click **Save**.
6. Wait for the deployment to complete.
7. Copy the published website URL and add it to the Project Links section above.

**Note:** GitHub Pages hosts static websites and does not run Python Flask applications. The Flask application requires a Python-compatible hosting environment if you want to deploy the backend online.

## 📌 Important Notes

* The dashboard and story are hosted on Tableau Public.
* An active internet connection is required to load embedded Tableau visualizations.
* The published Tableau workbooks must be publicly accessible for visitors to view them.
* The website provides access to the visualizations; the charts and underlying data are controlled by the published Tableau workbooks.

**Formula 1 Race Intelligence Platform** 🏎️
*An interactive data visualization project powered by Tableau Public.*

Abhay Sankhla

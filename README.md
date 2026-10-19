# Algorithm Visualizer

Animated visualizations of data structures and algorithms, built with [Manim](https://docs.manim.community/) and shown in a small React + TypeScript web app. Pick an algorithm from the dropdown and watch it run, step by step, with its time complexity.

**Live demo:** https://amirkasrajahan.github.io/algorithm-visualizer/

## What's inside

| Topic | Visualizations |
|---|---|
| Searching | Linear search, binary search |
| Sorting | Bubble sort, selection sort |
| Linked lists | Traversal, insertion |
| Stacks | Push, pop, valid parentheses (valid and invalid input), evaluate reverse polish notation |

Each animation shows the data structure, the pointers or markers involved, the key operation at every step (compare, swap, push, pop, relink), and the time complexity.

## How it works

1. Each algorithm is a Manim scene in `algorithms/`, written in Python.
2. `render.sh` renders every scene to an MP4 in `frontend/public/videos/`.
3. The React app in `frontend/` lists the algorithms (`frontend/src/algorithms.ts`) and plays the selected video.
4. The site is deployed to GitHub Pages, so it is just static files and needs no backend.

## Project structure

```
algorithms/        one file per topic: scenes written in Manim
basics/            early Manim practice (shapes, transforms, positioning)
frontend/          React + TypeScript (Vite) site
  src/algorithms.ts    the list of algorithms the dropdown is built from
  public/videos/       rendered animations
render.sh          renders all scenes into frontend/public/videos/
requirements.txt   Python dependencies
```

## Running it locally

### 1. Python and Manim

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Manim also needs `cairo`, `pkg-config` and `ffmpeg` on the system. On macOS: `brew install cairo pkg-config ffmpeg`.

### 2. Render the animations

```bash
./render.sh
```

To preview a single scene while you work on it:

```bash
manim -pql algorithms/linear_search.py LinearSearch
```

`-p` opens the video when it finishes and `-ql` renders at low quality for fast iteration. Use `-qm` for the quality the site uses.

### 3. Run the website

```bash
cd frontend
npm install
npm run dev
```

Then open http://localhost:5173/algorithm-visualizer/ (the path matches the GitHub Pages address).

## Adding an algorithm

1. Write the scene in `algorithms/` (or add a class to an existing file).
2. Add a line for it to the `SCENES` list in `render.sh`.
3. Add an entry (name, video path, complexity, description) to `frontend/src/algorithms.ts`.
4. Render it, check it in the local site, then deploy.

## Deploying

```bash
cd frontend
npm run deploy
```

This builds the site and publishes it to the `gh-pages` branch, which GitHub Pages serves.

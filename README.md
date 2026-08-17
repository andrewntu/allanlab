# cnliu.dev — personal site v2.0.0

Single-page static portfolio. No frameworks, no build step, no dependencies —
one HTML file + assets. Deployed on GitHub Pages.

## Structure
- `index.html` — the whole site (HTML + CSS + JS inline)
- `images/photo.jpg` — profile photo (also used as the social-share preview)
- `files/Resume_Cheng-Nan_Liu.pdf` — downloadable resume
- `.nojekyll` — tells GitHub Pages to skip the Jekyll build and serve files as-is

## How to update
- **Resume**: replace `files/Resume_Cheng-Nan_Liu.pdf` with the new PDF (keep the filename).
- **Text / jobs / papers**: everything is plain HTML in `index.html` — search for the
  section markers (`id="experience"`, `id="publications"`, …) and edit in place.
- **Photo**: replace `images/photo.jpg`.

## Deploy (replace old Jekyll site)
```bash
git clone https://github.com/andrewntu/cnliu_web.git
cd cnliu_web
git rm -r . && git clean -fdx        # wipe out old Jekyll site
cp -R /path/to/cnliu_site/. .        # copy these files in
git add -A
git commit -m "v2.0.0: redesign as static portfolio"
git push
```
Site goes live at https://andrewntu.github.io/cnliu_web/ within ~1 minute.

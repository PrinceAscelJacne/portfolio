# CV

Source du CV publié dans `public/CV_Prince_Ascel_DJIBODE.pdf`.

Pour régénérer le PDF après une modification de `cv.html` :

```sh
node cv/render.cjs "$PWD/cv/cv.html" "$PWD/public/CV_Prince_Ascel_DJIBODE.pdf"
```

Nécessite Playwright (`npm i -D playwright && npx playwright install chromium`).

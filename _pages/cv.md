---
title: "CV/Resume"
layout: textlay
excerpt: "Openings"
sitemap: false
permalink: /cv/
---

<div id="pdf-viewer" style="height: 800px;"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.16.105/pdf.min.js"></script>
<script>
    const url = '{{ site.url }}{{ site.baseurl }}/files/CN_CV_2024.pdf';
    const viewer = document.getElementById('pdf-viewer');
    pdfjsLib.getDocument(url).promise.then(function(pdf) {
        pdf.getPage(1).then(function(page) {
            const viewport = page.getViewport({ scale: 1.5 });
            const canvas = document.createElement('canvas');
            viewer.appendChild(canvas);
            const context = canvas.getContext('2d');
            canvas.height = viewport.height;
            canvas.width = viewport.width;
            page.render({ canvasContext: context, viewport: viewport });
        });
    });
</script>

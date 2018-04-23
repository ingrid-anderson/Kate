import sass
import os

sass.compile(dirname=('static/src/scss', 'static/dist'), output_style='compressed')

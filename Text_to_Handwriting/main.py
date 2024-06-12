import pywhatkit as pw

# text, path   # handwriting.png  # blue (default color)

txt="""I am Web Developer. I love codding. I listen Podcast
"""

pw.text_to_handwriting(txt, "deo.png", [0,0,138])
print("END")



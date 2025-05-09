Here's a guide to the basics of formatting using the `python-docx` module. We'll cover text formatting, font customization, tables, and general document styling.

---

## 1. **Text Formatting**

### Adding a Paragraph
```python
from docx import Document

doc = Document()
doc.add_paragraph("This is a plain paragraph.")
doc.save("example.docx")
```

### Adding a Heading
```python
doc.add_heading("This is a Heading", level=1)  # Levels range from 1 (largest) to 6 (smallest)
doc.save("example.docx")
```

### Aligning Text
```python
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

paragraph = doc.add_paragraph("This paragraph is centered.")
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
doc.save("example.docx")
```

---

## 2. **Font Customization**

### Changing Font Style and Size
```python
from docx.shared import Pt

paragraph = doc.add_paragraph("Customized font style.")
run = paragraph.add_run()
run.text = "This text is bold and 16pt."
run.bold = True
run.font.size = Pt(16)
doc.save("example.docx")
```

### Setting Font Name
```python
from docx.shared import RGBColor

run.font.name = "Arial"
run.font.color.rgb = RGBColor(0, 102, 204)  # Set text color to blue
doc.save("example.docx")
```

---

## 3. **Working with Tables**

### Creating a Simple Table
```python
table = doc.add_table(rows=2, cols=3)  # 2 rows, 3 columns
table.style = "Table Grid"

# Adding content to cells
table.cell(0, 0).text = "Header 1"
table.cell(0, 1).text = "Header 2"
table.cell(0, 2).text = "Header 3"
table.cell(1, 0).text = "Row 1, Col 1"
table.cell(1, 1).text = "Row 1, Col 2"
table.cell(1, 2).text = "Row 1, Col 3"

doc.save("example.docx")
```

### Formatting a Table
```python
from docx.enum.table import WD_ALIGN_VERTICAL

# Accessing a specific cell and customizing it
cell = table.cell(0, 0)
cell.paragraphs[0].alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
cell.text = "Centered Header"

doc.save("example.docx")
```

---

## 4. **Styling the Document**

### Applying a Style
```python
paragraph = doc.add_paragraph("Styled text.", style="Title")
doc.save("example.docx")
```

### List of Available Styles
```python
for style in doc.styles:
    print(style.name)  # Lists all available styles
```

---

## 5. **Adding Page Breaks**
```python
doc.add_paragraph("This is the first page.")
doc.add_page_break()
doc.add_paragraph("This is the second page.")
doc.save("example.docx")
```

---

## 6. **Headers and Footers**

### Adding a Header
```python
header = doc.sections[0].header
header.paragraphs[0].text = "This is a header"
doc.save("example.docx")
```

### Adding a Footer
```python
footer = doc.sections[0].footer
footer.paragraphs[0].text = "This is a footer"
doc.save("example.docx")
```

---

## 7. **Adding Images**

### Adding and Resizing Images
```python
from docx.shared import Inches

doc.add_picture("example.jpg", width=Inches(2), height=Inches(2))
doc.save("example.docx")
```

---

### Practice and Explore
With this foundation, you can experiment with combining these features to fit your project’s needs. For advanced tasks, consult the [python-docx documentation](https://python-docx.readthedocs.io/en/latest/).
# Import the FPDF class from the fpdf library, which is used for creating PDF documents.
from fpdf import FPDF
# Import the pandas library, which is used here for reading and manipulating data from a CSV file.
import pandas as pd

# Initialize the FPDF object (the PDF document).
# orientation="P": Sets the page orientation to Portrait.
# unit="mm": Sets the unit of measurement to millimeters.
# format="A4": Sets the standard page size to A4.
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Disable automatic page breaking. This gives manual control over when new pages are added.
# auto=False: Turns off automatic page breaking.
# margin=0: Sets the margin to 0 (though not strictly necessary since auto is False).
pdf.set_auto_page_break(auto=False, margin=0)

# Read data from the "topics.csv" file into a pandas DataFrame (df).
# Assuming "topics.csv" contains columns like "Topic" and "Pages".
df = pd.read_csv("topics.csv")

# Iterate over each row in the DataFrame. Each row represents a main topic.
for index, row in df.iterrows():
    # -----------------------------------------------------------
    # START of the MAIN Topic Page (The first page for the topic)
    # -----------------------------------------------------------

    # Add a new page to the PDF for the current topic.
    pdf.add_page()

    # Set the font for the main topic header.
    # family="Times": Uses the Times font.
    # style="B": Sets the style to Bold.
    # size=24: Sets the font size to 24 points.
    pdf.set_font(family="Times", style="B", size=24)

    # Set the text color for the header (mid-grey: R=100, G=100, B=100).
    pdf.set_text_color(100, 100, 100)

    # Output the Topic title on the page.
    # w=0: Width extends to the right margin (full width).
    # h=12: Height of the cell in mm.
    # txt=row["Topic"]: The text content is the value from the 'Topic' column in the current row.
    # align="L": Aligns text to the Left.
    # ln=1: Moves the current position to the beginning of the next line after outputting the cell.
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Draw a line below the main topic title.
    # Parameters are (x1, y1, x2, y2) coordinates in mm.
    # (10, 21) is the start point (10mm from left, 21mm from top).
    # (200, 21) is the end point (200mm from left, 21mm from top).
    pdf.line(10, 21, 200, 21)

    # Move the current position down by 265mm.
    # This effectively positions the cursor near the bottom of the A4 page for the footer.
    pdf.ln(265)

    # Set the font for the footer text.
    # style="I": Sets the style to Italic.
    # size=8: Sets the font size to 8 points.
    pdf.set_font(family="Times", style="I", size=8)

    # Set the text color for the footer (light-grey: R=180, G=180, B=180).
    pdf.set_text_color(180, 180, 180)

    # Output the Topic title as the footer on the main page.
    # align="R": Aligns text to the Right.
    # Note: ln=0 is the default, so the position does not move to the next line.
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # -----------------------------------------------------------
    # START of Additional Blank Pages for the Topic
    # -----------------------------------------------------------

    # Loop to create the required number of additional blank pages (minus the main page already created).
    # row["Pages"] gives the total pages needed, so we subtract 1.
    for i in range(row["Pages"] - 1):
        # Add the subsequent blank page.
        pdf.add_page()

        # Move the current position down by 277mm (positioning cursor near bottom).
        # NOTE: The original code used 'df.ln(277)' which seems like a typo.
        # It has been corrected to 'pdf.ln(277)' assuming the intention was to use the FPDF method.
        pdf.ln(277)

        # Set the font for the footer on the blank page.
        pdf.set_font(family="Times", style="I", size=8)

        # Set the text color for the footer.
        pdf.set_text_color(180, 180, 180)

        # Output the Topic title as the footer on the blank page.
        # This acts as a header/identifier for the continuation pages.
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

# Save the final generated PDF document to a file named "output.pdf".
pdf.output("output.pdf")
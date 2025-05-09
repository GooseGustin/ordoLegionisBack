import pypandoc
from airium import Airium

def generate_report():
    a = Airium()
    a('<!DOCTYPE html>')
    
    with a.html():
        with a.head():
            a.title(_t="Financial Report")
            a.style(_t="""
                body { font-family: Arial, sans-serif; }
                h1 { text-align: center; color: darkblue; }
                table { width: 100%; border-collapse: collapse; }
                th, td { border: 1px solid black; padding: 8px; text-align: left; }
                th { background-color: lightgray; }
            """)

        with a.body():
            a.h1(_t="Main Report Title", style="color: red; text-align: center; font-size: 24px; font-weight: bold;")
            a.p(_t="This is an introduction to the report.", style="font-style: italic; font-size: 14px; color: gray;")

            with a.table():
                with a.tr():
                    a.th(_t="Date")
                    a.th(_t="Description")
                    a.th(_t="Amount")

                with a.tr():
                    a.td(_t="2025-03-24")
                    a.td(_t="Office Supplies")
                    a.td(_t="$150.00")

                with a.tr():
                    a.td(_t="2025-03-25")
                    a.td(_t="Travel Expenses")
                    a.td(_t="$200.00")

            # Add an image
            a.img(src="Vexillium_Legionis.png", width="200px", height="100px", style="display: block; margin: auto;")

    # Save the HTML file
    html_file = "air_doc_4.html"
    with open(html_file, "w", encoding="utf-8") as file:
        file.write(str(a))

    # Convert to Word document
    docx_file = "air_doc_4.docx"
    pypandoc.convert_file(html_file, 'docx', outputfile=docx_file)

    print(f"Report successfully generated: {docx_file}")

# Run the function
generate_report()


# import pypandoc # type:ignore
# from airium import Airium # type:ignore

# def generate_report(): # curia, praesidium, report):
#     a = Airium()
#     a('<!DOCTYPE html>')
#     # print(dir(a.SINGLE_TAGS))

#     with a.html():
#         with a.head():
#             a.title(_t="Praesidium Annual Report")
#             a.style(_t="""
#                 body { font-family: Arial, sans-serif; }
#                 h1 { text-align: center; color: darkblue; }
#                 table { width: 100%; border-collapse: collapse; }
#                 th, td { border: 1px solid black; padding: 8px; text-align: left; }
#                 th { background-color: lightgray; }
#             """)

#         with a.body():
#             a.h1(_t="Financial Summary Report")
#             a.p(_t="Generated using Airium.")

#             with a.table():
#                 with a.tr():
#                     a.th(_t="Date")
#                     a.th(_t="Description")
#                     a.th(_t="Amount")

#                 with a.tr():
#                     a.td(_t="2025-03-24")
#                     a.td(_t="Office Supplies")
#                     a.td(_t="$150.00")

#                 with a.tr():
#                     a.td(_t="2025-03-25")
#                     a.td(_t="Travel Expenses")
#                     a.td(_t="$200.00")

#             a.img(src='./Vexillium_Legionis.png', width='200px', height='100px', style='display: block; margin: auto;')

#     # Save the file 
#     file_name = "air_doc_1"
#     html_file = f'{file_name}.html'
#     with open(html_file, 'w', encoding='utf-8') as file: 
#         file.write(str(a))

#     # Convert to word document
#     docx_file = f'{file_name}.docx'
#     pypandoc.convert_file(html_file, 'docx', outputfile=docx_file)

#     print(f"Report successfully generated: {docx_file}")


# generate_report()
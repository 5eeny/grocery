from jinja2 import Template

'''TEMPLATE = """This is {p:+} and this is {n:+}"""  #specifier : brings the sign of the number
TEMPLATE2 = """Hello {{name}}"""

print(TEMPLATE.format(p=5, n=-7))
template = Template(TEMPLATE2)
print(template.render(name='woah'))'''

some_data =[
    {"id" : 34, "foody" : "tastemaster", "category" : "maggi"},
    {"id" : 34, "foody" : "tastemaster", "category" : "maggi"}
]

def main():
    print("hello world")
    template_file = open("F:/IITM BSc/Mad1/ProjectGS/table/some_data.html.jinja2")
    TEMPLATE = template_file.read()
    template_file.close()

    template = Template(TEMPLATE)
    content = template.render(some_data=some_data)

    htm_doc_file = open('some.html','w')
    htm_doc_file.write(content)
    htm_doc_file.close()

if __name__ == "__main__":
    main()


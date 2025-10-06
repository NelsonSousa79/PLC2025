import re

def replace_match(m):
    if m.group(1): return f'<h1>{m.group(1)}</h1>'
    if m.group(2): return f'<h2>{m.group(2)}</h2>'
    if m.group(3): return f'<h3>{m.group(3)}</h3>'
    if m.group(4): return f'<b>{m.group(4)}</b>'
    if m.group(5): return f'<i>{m.group(5)}</i>'
    if m.group(6): return f'<li>{m.group(6)}</li>'  
    if m.group(7): return f'<a href="{m.group(8)}">{m.group(7)}</a>'
    if m.group(9): return f'<img src="{m.group(10)}" alt="{m.group(9)}"/>'
    return m.group(0)


markdown = """# Título
## Subtítulo
**negrito**
*itálico*
1. Primeiro item
2. Segundo item
3. Terceiro item
Link: [UC](http://uc.pt)
Imagem: ![coelho](http://coelho.com)"""


html = re.sub(
    r'^# (.+)$|^## (.+)$|^### (.+)$|\*\*(.+?)\*\*|\*(.+?)\*|^\d+\.\s+(.+)$|\[(.+?)\]\((.+?)\)|!\[(.+?)\]\((.+?)\)',
    replace_match, markdown, flags=re.MULTILINE
)

# Adiciona <ol> e </ol> ao redor dos <li> no caso de lista e a flag re.DOTALL para o ponto "."
# corresponder a qualquer caractere INCLUINDO quebra de linha (\n).

html = re.sub(r'(<li>.*</li>)', r'<ol>\n\1\n</ol>', html, flags=re.DOTALL)

print("HTML convertido:")
print(html)
from pathlib import Path
import sys

from jinja2 import Environment, FileSystemLoader

get_tmpl = Environment(loader=FileSystemLoader('templates/')).get_template


def extract_slide_title(md_file):
    with md_file.open() as f:
        for l in f:
            if '#' in l:
                return l.strip('# \n')


def get_md_files():
    p = Path('content', 'slides')
    for md_file in sorted(p.iterdir()):
        if md_file.suffix == '.md':
            yield str(md_file), md_file.with_suffix('.html').name, extract_slide_title(md_file)


def pre_clean():
    p = Path('.')
    for i in p.glob('*.html'):
        i.unlink()


def main():
    pre_clean()

    slide_tmpl, index_tmpl = get_tmpl('slide.j2'), get_tmpl('index.j2')

    md_files = list(get_md_files())

    for md_file, html_file, title in md_files:
        rendered_template = slide_tmpl.render(mdfile=md_file, title=title)

        with open(html_file, 'w') as f:
            f.write(rendered_template)

    with open('index.html', 'w') as f:
        f.write(index_tmpl.render(slides=md_files))


if __name__ == '__main__':
    sys.exit(main())

from user_interfece import decimal_view
from user_interfece import fraction_view
from user_interfece import comprehensiven_view
from user_interfece import calculator_view

def create(device = 1):
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '      <p {}>decimal: {} c</p>\n'\
        .format(style, decimal_view(device))
    html += '      <p {}>decimal: {} c</p>\n'\
        .format(style, fraction_view(device))
    html += '      <p {}>decimal: {} c</p>\n'\
        .format(style, comprehensiven_view(device))
    html += '      <p {}>decimal: {} c</p>\n'\
        .format(style, calculator_view(device))
    
    with open('index.html', 'w') as page:
        page.write(html)

    return html  
    
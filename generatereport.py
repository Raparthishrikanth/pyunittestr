from tabulate import tabulate

table = [['one','two','three'],['four','five','six'],['seven','eight','nine']]
print(tabulate(table,tablefmt='html'))

with open('example.log') as f:
    lines = f.readlines()
    print(lines)
    print(lines[2])

HTML_file=open("Report.html","w+")
HTML_file.write("<html>\n <table border=1>\n <tr>\n <td>"+lines[2]+"</td>\n </tr> \n </table>\n </html>")
print(tabulate(lines, tablefmt='html'))
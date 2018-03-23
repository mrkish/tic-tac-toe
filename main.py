from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True





page_header = """
    <!doctype html>
        <html>
            <head>
                <title>Tic-Tac-Toe!</title>
            </head>
            <body>
        
        """

page_footer = """
            </body>
        </html>
        """




@app.route('/')
def index():

    return page_header + page_footer



if __name__ == "__main__":
    app.run()

from validator import app

def main():
    from paste import httpserver
    httpserver.serve(app, host='localhost', port='8080')

if __name__ == '__main__':
    main()
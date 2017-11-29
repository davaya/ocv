from validator import app

def main():
    from paste import httpserver
    from paste.cascade import Cascade
    from webob.static import DirectoryApp, FileApp

# Create a cascade that looks for static files first, then tries the webapp
    static_app = DirectoryApp("static")
    fullapp = Cascade([static_app, app])
    httpserver.serve(fullapp, host='localhost', port='8070')

if __name__ == '__main__':
    main()
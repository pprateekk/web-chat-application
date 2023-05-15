from webApplication import app

#checks whether the module is being run as the main program or being imported as a module into another
if __name__ == '__main__':
    app.run(debug=True)

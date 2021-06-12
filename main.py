from music import create_app

# launch the application

if __name__=='__main__':
    napp=create_app()
    napp.run(debug=True)
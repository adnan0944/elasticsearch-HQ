from elastichq import factory

application = factory.create_app()

if __name__ == '__main__':
    application.run(debug=False, threaded=True, use_reloader=True)
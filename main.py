from werkzeug.serving import run_simple

from bnetprofile import app


def main():
    run_simple("localhost", 5001, app, threaded=True, ssl_context='adhoc')


if __name__ == "__main__":
    main()

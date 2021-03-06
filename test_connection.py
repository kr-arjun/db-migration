from dbclient import *
import sys

# python 3.6

def main():
    # define a parser to identify what component to import / export
    parser = get_export_parser()
    # parse the args
    args = parser.parse_args()
    p = args.profile

    # parse the path location of the Databricks CLI configuration
    login_creds = get_login_credentials(profile=p)

    # parse the credentials
    url = login_creds['host']
    token = login_creds['token']
    export_dir = 'logs/'

    print("Test connection at {0} with profile {1}\n".format(url, args.profile))
    db_client = dbclient(token, url, export_dir)
    try:
        is_successful = db_client.test_connection()
    except requests.exceptions.RequestException as e:
        print(e)
        print("\nUnsuccessful connection. Verify credentials.\n")
        sys.exit(1)
    if is_successful == 0:
        print("Connection successful!")
    else:
        print("\nUnsuccessful connection. Verify credentials.\n")

if __name__ == '__main__':
    main()

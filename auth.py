# Imports the necessary package to perform JWT Authentication
from boxsdk import JWTAuth

# Creates an auth object
auth = JWTAuth(
    
    client_id='<my client_id>', 
    client_secret='<my client secret>', 
    enterprise_id='<my enterprise id>',
    jwt_key_id='<my public key id>',
    
    # System path to your private key file.
    rsa_private_key_file_sys_path='private_key.pem',
    # The password that the private key was generated with (comment out if none)
    #rsa_private_key_passphrase=''
)

# generate an enterprise token for use with PostMan
enterprise_token = auth.authenticate_instance()
print enterprise_token;

# Imports the package to create an authenticated Client
from boxsdk import Client

# Creates a client used for performing actions through the API
client = Client(auth)


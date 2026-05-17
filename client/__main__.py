import socket
from dto.body import Body
from dto.header import Header
from client.implementations.client_request_handler import ClientRequestHandler

NEW_LINE = '\n'
MANDATORY_HEADERS = ["host", 'port', 'content_type']

def get_client_header(content_length):
    header = Header()
    headers_input = {key: input(f"{key}: ") for key in MANDATORY_HEADERS}
    headers_input['content_length'] = content_length
    header.set_header(headers_input)
    return header

def get_client_body():
    body = Body()
    body_input = input("body : ")
    body_length = len(body_input.encode())
    body.set_body(body_input)
    return body, body_length


if __name__ == '__main__':
    print("[CLIENT] Start the client process")
    print('****************************************')

    print("[CLIENT] Getting headers ")
    print('****************************************')

    body, body_length = get_client_body()
    header = get_client_header(body_length)
    #header = "this is the header we're using"

    print("[CLIENT] Start the Socket ")
    print('****************************************')
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        address = (header.get_header_values('host'), int(header.get_header_values('port')))
        #address = (('localhost', 9999))
        # start client connection
        s.connect(address)
        
        # call the request client request handler
        crh = ClientRequestHandler(header, body)
        request = crh.handle()
        s.sendall(request)
        response = s.recv(1024)
        print(response.decode())

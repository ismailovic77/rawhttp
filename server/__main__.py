import socketserver
from server.handler import Handler

if __name__ == '__main__':
    HOST, PORT = ("localhost", 9999)
    with socketserver.TCPServer((HOST,PORT), Handler) as server:  
        """
        here we essentially created a server , this replaces the creation of the socket for TCP , calling the bind and the listen 
        the difference is that there is some checks happening before , but essentially it does this 
        """
        print(f"[Starting server] server listening on {HOST}:{PORT}")

        server.serve_forever()
        """
        This internally calls the get_request() , that will call the accept() method to return the request object (new connection
        object with the adress of the client that connected), here the server is blocked until receiving a client connection
        
        once a client connects, we call the finish_request() that will create the instance of MyHandler class with the 
        request and adress passed as params . The init function of Myhandler class will use the super() constructor to setup
        the server variables and then call the setup(), handle() and finish() function that will work only on the request

        So basically in the code of my handler I know that the request variable has been setup so I can receive the data from
        the client
        """



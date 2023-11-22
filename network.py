import select

class DataExchanger:

    def __init__(self, dst, src):
        self.dst = dst
        self.src = src

    def exchange_data(self):
        while True:
            # wait until client or remote is available for read
            read_sockets, _, _ = select.select([self.dst, self.src], [], [], 0.1)

            for socks in read_sockets:
                if socks == self.dst:
                    
                    data = self.dst.recv(4096)
                    #print("SEND",data)
                    if len(data) == 0:  # Verifica se la connessione è stata chiusa
                        return
                    self.src.sendall(data)
                elif socks == self.src:
                    
                    data = self.src.recv(4096)
                    #print("RECV",data)
                    if len(data) == 0:  # Verifica se la connessione è stata chiusa
                        return
                    self.dst.sendall(data)
        
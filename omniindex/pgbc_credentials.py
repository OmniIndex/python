from credentials import BasicCredentials

class PGBCCredentials(BasicCredentials):
    def __init__(self, data_source: str, username: str = '', password: str = '', server: str = 'localhost', port: int = 5432):
        super().__init__(username, password)
        self.dataSource = data_source
        self.server = server
        if isinstance(port, int) and 5430 <= port <= 5435:
            self.port = port
        else:
            raise ValueError("Invalid port number")

    def are_valid(self):
        if not isinstance(self.port, int) or self.port < 5430 or self.port > 5435:
            return False
        return bool(self.server) and bool(self.dataSource) and bool(self.port) and bool(self.username) and bool(self.password) and super().are_valid()

    def __str__(self):
        return f"PGBCCredentials(dataSource={self.dataSource}, username={self.username}, password={self.password}, server={self.server}, port={self.port})"

    def __repr__(self):
        return f"PGBCCredentials(dataSource={self.dataSource}, username={self.username}, password={self.password}, server={self.server}, port={self.port})"
